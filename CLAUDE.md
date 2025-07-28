# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## High-Level Architecture

This is a cross-platform desktop GUI application for image processing, built with Python.

- **GUI Framework:** The user interface is built using `tkinter` via the `ttkbootstrap` library for a modern look and feel. The main UI code is located in `fotokilof/gui.py`.
- **Image Processing:** The core functionality relies on the ImageMagick library, accessed through the `wand` Python wrapper. It uses `Pillow` as a fallback if ImageMagick is not available. The image conversion logic is split across:
    - `fotokilof/convert_wand.py`: For ImageMagick-based operations.
    - `fotokilof/convert_pillow.py`: For Pillow-based operations.
    - `fotokilof/convert.py`: A likely wrapper or dispatcher for the above modules.
- **Entry Point:** The application is launched from `fotokilof/__main__.py`.
- **Configuration:** Application settings are handled by `fotokilof/ini_read.py` and `fotokilof/ini_save.py`.
- **Internationalization (i18n):** Localization is supported through `.po` files located in the `fotokilof/locale/` directory.

## Common Development Commands

The project uses `setuptools` and `pyproject.toml` for packaging.

### Setting up the Development Environment

1.  **Install system dependencies:**
    - **Linux (Debian/Ubuntu):**
      ```bash
      sudo apt-get install python3-pip python3-tk python3-wand imagemagick xclip
      ```
    - **macOS (using Homebrew):**
      ```bash
      brew install imagemagick python-tk
      ```
    - **Windows:**
      - Install [Python 3.10+](https://www.python.org/).
      - Install [ImageMagick](https://imagemagick.org/script/download.php#windows), ensuring you add it to the system `PATH` and install the necessary development libraries/headers.

2.  **Install Python packages in editable mode:**
    From the root of the repository, run:
    ```bash
    python3 -m pip install -e .
    ```

### Running the Application

To run the application for development:
```bash
python3 -m fotokilof
```
or simply:
```bash
fotokilof
```

### Internationalization (i18n)

To update translation files after adding new translatable strings in the code:
```bash
sh scripts/4_generate_pot.sh
```
This will update the `fotokilof.pot` template file. You can then use a tool like Poedit to update the language-specific `.po` files in `fotokilof/locale/`.

### Linting and Testing

The project does not have a pre-configured linter or an automated test suite. When making changes, ensure your code is clean, and manually test the application's functionality thoroughly.
