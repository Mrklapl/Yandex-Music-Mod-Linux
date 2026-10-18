# 🎵 Яндекс Музыка Мод для Linux (AppImage)

[![Release](https://img.shields.io/badge/Версия-5.97.3--2.23.2-blue.svg)](https://github.com/Vzlomhik2005/Yandex-Music-Mod/releases)
[![Platform](https://img.shields.io/badge/Платформа-Linux%20(AppImage)-orange.svg)](https://appimage.org/)
[![Status](https://img.shields.io/badge/Статус-Стабильный-success.svg)]()
[![Privacy](https://img.shields.io/badge/Аккаунты-100%25%20Clean-brightgreen.svg)]()

Полноценная сборка популярного мода **Яндекс Музыки** в формате **AppImage** для Linux с эксклюзивными исправлениями интерфейса, стабильной навигацией и полной поддержкой «Кольца интересов» в «Моей волне».

---

## ✨ Возможности и преимущества

- 🔓 **Работа без подписки «Плюс»**: обход ограничений бесплатного тарифа.
- 🎧 **Максимальное качество звука**: прослушивание в High Quality и Lossless/FLAC.
- 🎡 **Исправленное «Кольцо интересов»**:
  - Устранена ошибка исчезновения колеса при переключении на «Назад к привычному».
  - Предотвращено опустошение списка карточек и блокировка обновления в хранилище MobX.
  - Добавлены отказоустойчивые резервные пресеты и автоматическое восстановление состояния.
- 🧭 **Стабильная навигация по всем вкладкам**:
  - Полностью устранены ошибки `Что-то пошло не так` при переходах между разделами («Поиск», «Концерты», «Книги и подкасты», «Детям», «Коллекция»).
- 🚫 **Без рекламы и аналитики**: вырезаны рекламные вставки, трекеры и баннеры.
- 💜 **Интеграция с Discord**: поддержка Rich Presence с отображением текущего трека и статуса.
- 🎤 **Тексты песен**: синхронизированные караоке-тексты через базу [LRCLib](https://lrclib.net).
- ⬇️ **Скачивание треков**: встроенная загрузка музыки в локальные аудиофайлы через ffmpeg.
- 🪟 **Интеграция с Linux Desktop**:
  - Поддержка закрытия в системный трей (Close to Tray).
  - Корректная работа под Wayland (Hyprland, Sway, GNOME, KDE) и X11.

---

## 🔒 Безопасность и приватность

> [!IMPORTANT]
> **В сборке отсутствуют какие-либо персональные данные, сессии или аккаунты.**
> Все авторизационные токены, куки и локальные базы данных генерируются исключительно на стороне пользователя и хранятся локально в `~/.config/YandexMusic`. Репозиторий и AppImage на 100% чисты.

---

## 🚀 Установка и запуск

### Вариант 1: Запуск готового AppImage
1. Скачайте файл `YandexMusicMod-5.97.3-2.23.2.linux.AppImage` из раздела [Releases](releases).
2. Сделайте файл исполняемым:
   ```bash
   chmod +x YandexMusicMod-5.97.3-2.23.2.linux.AppImage
   ```
3. Запустите двойным кликом или через терминал:
   ```bash
   ./YandexMusicMod-5.97.3-2.23.2.linux.AppImage
   ```

### Вариант 2: Добавление ярлыка в меню приложений
Создайте файл `~/.local/share/applications/yandex-music.desktop`:
```ini
[Desktop Entry]
Name=Яндекс Музыка
Comment=Слушайте треки, подкасты и Мою волну без ограничений
Exec=/home/user/Downloads/YandexMusicMod-5.97.3-2.23.2.linux.AppImage %U
Icon=/home/user/.local/share/icons/yandex-music.png
Terminal=false
Type=Application
Categories=Audio;Music;Player;
StartupWMClass=YandexMusicMod
StartupNotify=true
MimeType=x-scheme-handler/yandexmusic;
```
*(замените `user` на имя вашей учетной записи Linux)*

---

## 🛠️ Сборка из исходников

Для сборки требуются: `node`, `bun`, `mksquashfs`, `asar`.

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Mrklapl/Yandex-Music-Mod-Linux.git
   cd Yandex-Music-Mod-Linux
   ```
2. Примените патчи интерфейса и колеса интересов:
   ```bash
   python3 scripts/apply-wheel-patch.py
   ```
3. Соберите AppImage:
   ```bash
   bash scripts/build-appimage.sh
   ```

---

## 🙏 Благодарности и первоисточники

- [Vzlomhik2005/Yandex-Music-Mod](https://github.com/Vzlomhik2005/Yandex-Music-Mod) — базовые патчи обхода подписки, встроенные скрипты и расширения функционала.
- [Stephanzion/YandexMusicBetaMod](https://github.com/Stephanzion/YandexMusicBetaMod) / [Asisstant335](https://github.com/Asisstant335/YandexMusicBetaMod) — ранние наработки портирования на Linux.
- [LRCLib](https://lrclib.net) — база текстов песен и караоке.

---

## ⚖️ Дисклеймер
Данный проект создан исключительно в ознакомительных и исследовательских целях. Все права на бренд «Яндекс Музыка» принадлежат компании ООО «Яндекс.Медиасервисы». Рекомендуется оформить официальную подписку «Яндекс Плюс» для поддержки правообладателей и исполнителей.
