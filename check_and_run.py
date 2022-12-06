# Copyright 2022 Abhishek Harshvardhan Mishra
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os
import re
import argparse
import subprocess
import sys


# The dependencies and utilities required by the scraper program.
# The URLs are used to download the dependencies and utilities.
# The commands are used to install the dependencies and utilities.
# If a command is None, then the dependency or utility is already
# installed and does not need to be installed.
DEPENDENCIES = [
    {
        "name": "beautifulsoup4",
        "url": "https://pypi.org/project/beautifulsoup4/",
        "command": "pip install beautifulsoup4",
    },
    {
        "name": "python-docx",
        "url": "https://pypi.org/project/python-docx/",
        "command": "pip install python-docx",
    },
    {
        "name": "openpyxl",
        "url": "https://pypi.org/project/openpyxl/",
        "command": "pip install openpyxl",
    },
    {
        "name": "pdfminer.six",
        "url": "https://pypi.org/project/pdfminer.six/",
        "command": "pip install pdfminer.six",
    },
]

def check_dependencies() -> bool:
    """Check if the dependencies and utilities required by the scraper
    program are installed on the system. Return True if all dependencies
    and utilities are installed, or False if any are missing.
    """
    for dep in DEPENDENCIES:
        if dep["command"] is None:
            continue  # this dependency is already installed

        # Check if the dependency or utility is installed by running
        # the installation command and checking the exit code.
        exit_code = subprocess.call(dep["command"], shell=True)
        if exit_code != 0:
            return False
    return True


def install_dependencies(proxy: str) -> None:
    """Install the dependencies and utilities required by the scraper
    program using the specified proxy server.
    """
    for dep in DEPENDENCIES:
        if dep["command"] is None:
            continue  # this dependency is already installed

        # Set the HTTP_PROXY and HTTPS_PROXY environment variables
        # to use the specified proxy server.
        os.environ["HTTP_PROXY"] = proxy
        os.environ["HTTPS_PROXY"] = proxy

        # Install the dependency or utility using the specified
        # installation command.
        print(f"Installing {dep['name']} from {dep['url']}")
        exit_code = subprocess.call(dep["command"], shell=True)
        if exit_code != 0:
            print(f"Failed to install {dep['name']}")


def check_and_run() -> None:
    """Check if the dependencies and utilities required by the scraper
    program are installed on the system, and install them if they
    are not present. Then run the scraper program using the provided
    command-line arguments.
    """
    if not check_dependencies():
        # Prompt the user to enter a proxy server to use when
        # downloading the dependencies and utilities.
        proxy = input("Enter a proxy server (e.g. http://proxy.example.com:8080): ")

        # Install the missing dependencies and utilities using the
        # specified proxy server.
        install_dependencies(proxy)

    # Run the scraper program using the provided command-line arguments.
    scraper_args = ["python", "scraper.py"] + sys.argv[1:]
    subprocess.call(scraper_args)


if __name__ == "__main__":
    check_and_run()