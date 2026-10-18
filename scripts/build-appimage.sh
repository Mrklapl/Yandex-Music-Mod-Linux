#!/usr/bin/env bash
set -e

# Build script for Yandex Music Mod Linux AppImage
# Requirements: bun / bunx, mksquashfs, node

WORKDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "==> Building Yandex Music Mod AppImage in: ${WORKDIR}"

INSPECT_DIR="${WORKDIR}/inspect_asar"
if [ ! -d "${INSPECT_DIR}" ] && [ -d "${WORKDIR}/../inspect_asar" ]; then
    INSPECT_DIR="${WORKDIR}/../inspect_asar"
fi

if [ ! -d "${INSPECT_DIR}" ]; then
    echo "ERROR: inspect_asar directory not found!"
    exit 1
fi

TMP_DIR="$(mktemp -d -t yandex_rebuild_XXXXXX)"
trap "rm -rf ${TMP_DIR}" EXIT

echo "==> Packaging ASAR archive from ${INSPECT_DIR}..."
bunx asar pack "${INSPECT_DIR}" "${TMP_DIR}/new_app.asar" --unpack "**/ffmpeg-static/**"

# If a base AppImage exists, extract and replace resources
BASE_APPIMAGE="${1:-/home/xox/Downloads/YandexMusicMod-5.97.3-2.23.2.linux.AppImage}"
if [ ! -f "${BASE_APPIMAGE}" ]; then
    echo "ERROR: Base AppImage not found at ${BASE_APPIMAGE}"
    exit 1
fi

echo "==> Extracting runtime from base AppImage..."
head -c 188392 "${BASE_APPIMAGE}" > "${TMP_DIR}/runtime"

echo "==> Extracting base AppImage filesystem..."
(cd "${TMP_DIR}" && "${BASE_APPIMAGE}" --appimage-extract > /dev/null)

echo "==> Updating resources in squashfs-root..."
cp "${TMP_DIR}/new_app.asar" "${TMP_DIR}/squashfs-root/resources/app.asar"
rm -rf "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked"
cp -r "${TMP_DIR}/new_app.asar.unpacked" "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked"

# Ensure ffmpeg binary permissions
if [ -f "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked/node_modules/ffmpeg-static/ffmpeg" ]; then
    chmod +x "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked/node_modules/ffmpeg-static/ffmpeg"
fi

echo "==> Patching AppRun for auto Wayland ozone support (fixes invisible cursor on Wayland/Hyprland)..."
sed -i 's|exec "$BIN"|exec "$BIN" ${WAYLAND_DISPLAY:+--ozone-platform-hint=auto --enable-features=WaylandWindowDecorations}|g' "${TMP_DIR}/squashfs-root/AppRun"

echo "==> Compressing Squashfs filesystem..."
mksquashfs "${TMP_DIR}/squashfs-root" "${TMP_DIR}/app.squashfs" -comp gzip -b 131072 -no-fragments

OUTPUT_APPIMAGE="${WORKDIR}/YandexMusicMod-5.97.3-2.23.2.linux.AppImage"
echo "==> Combining runtime and squashfs into ${OUTPUT_APPIMAGE}..."
cat "${TMP_DIR}/runtime" "${TMP_DIR}/app.squashfs" > "${OUTPUT_APPIMAGE}"
chmod +x "${OUTPUT_APPIMAGE}"

echo "==> Build complete: ${OUTPUT_APPIMAGE}"
ls -lh "${OUTPUT_APPIMAGE}"
