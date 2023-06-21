# Skyrage/Fractureiser Remover (SkyRev)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Skyrage/Fractureiser Remover (SkyRev) is a Python script that scans and updates JAR files, removing the 'javassist' directory if it exists. It provides a convenient way to clean up JAR files that may have been infected with the Skyrage/Fractureiser malware.

## Features

- Scans JAR files for the virus "Skyrage"
- Removes anything found to be malicious inside the JAR file
- Removes 'Javassist' and 'MainL10.class' files

## Prerequisites

- Python 3.x
- `colorama` library: Install it using `pip install colorama`
- `pyinstaller` library: Install it using `pip install pyinstaller`

## Usage

1. Clone this repository or download the script `SkyRev.py` to your local machine.
2. Install the `colorama` library by running the command `pip install colorama`.
3. Open a terminal or command prompt and navigate to the directory containing the `SkyRev.py` script.
4. Run the script and input the infected directory and the clean directory.
5. Let it scan and complete the cleaning process.

## Building

1. Open a terminal or command prompt and navigate to the directory containing the `SkyRev` script.
2. Install the `pyinstaller` library by running the command `pip install pyinstaller`.
3. Once in the directory that has `SkyRev.py`, run the command `pyinstaller --onefile skyrev.py`.
4. After it finishes building, go to the `dist` directory, and you will find the output file there.
5. Now you can use the built executable to scan your system.

## Issues and Feedback

Please report any issues you encounter at [GitHub Issues](https://github.com/wokonly/skyrev/issues). You can also join the Discord server for feedback and assistance at [Discord](https://discord.gg/VAx9qUsfhw).
