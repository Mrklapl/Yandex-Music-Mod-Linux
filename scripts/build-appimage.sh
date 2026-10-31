#!/usr/bin/env bash
set -e

# Build script for Yandex Music Mod Linux AppImage
# Requirements: bun / bunx, mksquashfs, node, python3

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

BASE_VERSION=$(node -e 'try{console.log(JSON.parse(require("fs").readFileSync(process.argv[1]+"/package.json")).version)}catch(e){console.log("5.125.3")}' "${INSPECT_DIR}")
MOD_VERSION="2.23.2"
APP_VERSION="${BASE_VERSION}-${MOD_VERSION}"
echo "==> Target version: ${APP_VERSION} (Base: ${BASE_VERSION}, Mod: ${MOD_VERSION})"

echo "==> Ensuring modern chunk patches & Plus unlock are applied..."
python3 "${WORKDIR}/scripts/apply-wheel-patch.py" "${INSPECT_DIR}"

TMP_DIR="$(mktemp -d -t yandex_rebuild_XXXXXX)"
trap "rm -rf ${TMP_DIR}" EXIT

echo "==> Packaging ASAR archive from ${INSPECT_DIR}..."
bunx asar pack "${INSPECT_DIR}" "${TMP_DIR}/new_app.asar" --unpack "**/ffmpeg-static/**"

# If a base AppImage exists, extract and replace resources
BASE_APPIMAGE="${1}"
if [ -z "${BASE_APPIMAGE}" ]; then
    BASE_APPIMAGE=$(ls -t "${WORKDIR}"/YandexMusicMod-*.AppImage "${WORKDIR}"/../*.AppImage 2>/dev/null | head -n 1 || true)
fi

if [ -z "${BASE_APPIMAGE}" ] || [ ! -f "${BASE_APPIMAGE}" ]; then
    echo "ERROR: Base AppImage not found. Please provide path to existing AppImage as argument: $0 <path-to-appimage>"
    exit 1
fi

echo "==> Using base AppImage: ${BASE_APPIMAGE}"
echo "==> Extracting runtime from base AppImage..."
head -c 188392 "${BASE_APPIMAGE}" > "${TMP_DIR}/runtime"

echo "==> Extracting base AppImage filesystem..."
(cd "${TMP_DIR}" && "${BASE_APPIMAGE}" --appimage-extract > /dev/null)

echo "==> Updating resources in squashfs-root..."
cp "${TMP_DIR}/new_app.asar" "${TMP_DIR}/squashfs-root/resources/app.asar"
rm -rf "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked"
if [ -d "${TMP_DIR}/new_app.asar.unpacked" ]; then
    cp -r "${TMP_DIR}/new_app.asar.unpacked" "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked"
fi

# Ensure ffmpeg binary permissions
if [ -f "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked/node_modules/ffmpeg-static/ffmpeg" ]; then
    chmod +x "${TMP_DIR}/squashfs-root/resources/app.asar.unpacked/node_modules/ffmpeg-static/ffmpeg"
fi

# Update desktop file version metadata
if [ -f "${TMP_DIR}/squashfs-root/yandexmusicmod.desktop" ]; then
    sed -i "s|^X-AppImage-Version=.*|X-AppImage-Version=${APP_VERSION}|g" "${TMP_DIR}/squashfs-root/yandexmusicmod.desktop"
fi

echo "==> Patching AppRun for auto Wayland ozone support (fixes invisible cursor on Wayland/Hyprland)..."
if ! grep -q "ozone-platform-hint" "${TMP_DIR}/squashfs-root/AppRun"; then
    sed -i 's|exec "$BIN"|exec "$BIN" ${WAYLAND_DISPLAY:+--ozone-platform-hint=auto --enable-features=WaylandWindowDecorations}|g' "${TMP_DIR}/squashfs-root/AppRun"
fi

echo "==> Compressing Squashfs filesystem..."
mksquashfs "${TMP_DIR}/squashfs-root" "${TMP_DIR}/app.squashfs" -comp gzip -b 131072 -no-fragments

OUTPUT_APPIMAGE="${WORKDIR}/YandexMusicMod-${APP_VERSION}.linux.AppImage"
echo "==> Combining runtime and squashfs into ${OUTPUT_APPIMAGE}..."
cat "${TMP_DIR}/runtime" "${TMP_DIR}/app.squashfs" > "${OUTPUT_APPIMAGE}"
chmod +x "${OUTPUT_APPIMAGE}"

echo "==> Build complete: ${OUTPUT_APPIMAGE}"
ls -lh "${OUTPUT_APPIMAGE}"
