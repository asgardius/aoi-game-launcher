# aoi-game-launcher

<img src=https://git.asgardius.company/asgardius/aoi-game-launcher/raw/branch/master/data/asgardius.page.aoilauncher.png>

A launcher for an anime role playing game game

This launcher download background music track when running for first time

All content is saved inside ~/.local/share/asgardius

# Dependencies

* python
* GTK 3
* VTE 3
* Pygame for music playback
* wget for updater

# Build dependencies
* Meson
* Ninja

# Install instructions
To build this app

meson . _build

To install

sudo ninja -C _build install

To uninstall

sudo ninja -C _build uninstall
