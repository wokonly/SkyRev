# Skyrage/Fractureiser Remover (SkyRev)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Skyrage/Fractureiser Remover (SkyRev) is a Python script that scans and updates JAR files, removing the 'javassist' directory if it exists. It provides a convenient way to clean up JAR files that may have been infected with the Skyrage/Fractureiser malware.

## Features

- Scans a directory for JAR files
- Checks if the 'javassist' directory exists in the JAR files
- Removes the 'javassist' directory from the infected JAR files
- Creates new clean versions of the JAR files without the 'javassist' directory

## Prerequisites

- Python 3.x
- `colorama` library: Install it using `pip install colorama`

## Usage

1. Clone this repository or download the script `SkyRev.py` to your local machine.
2. Install the `colorama` library by running `pip install colorama`.
3. Open a terminal or command prompt and navigate to the directory containing the `SkyRev.py` script.
4. Run the script and input the infected directory and the clean directory
5. Let it scan and done
