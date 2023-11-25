#!/usr/bin/env python
#
# Musort - A command-line tool for effortlessly organizing and renaming your music files based on metadata
# Copyright (C) 2023 tdeerenberg
#
# Sources on github:
# https://github.com/tdeerenberg/Musort
#
# Licensed under the GNU General Public License v3.0 (GPLv3)
# Copyright (C) 2023 tdeerenberg
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import getopt
import logging
from config import *
from variables import *
from tinytag import TinyTag

class Musort:
    def __init__(self):
        """Initial setup"""
        self.recursive = recursive
        self.separator = separator
        self.format = name_format.split('.')
        self.replace = forbidden_char_replace
        self.directory = None
        self.files = []
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s - %(message)s')

    def display_settings(self):
        """Displays the settings"""
        logging.info(f"Recursive renaming: '{self.recursive}'.")
        logging.info(f"Separator: '{self.separator}'.")
        logging.info(f"Format: {self.format}.")

    def get_files(self):
        """Check files from the given directory"""
        if self.recursive:
            self.files = [
                os.path.join(root, filename)
                for root, _, files in os.walk(self.directory)
                for filename in files
                if self.is_compatible(filename)
            ]
        else:
            self.files = [
                os.path.join(os.path.abspath(self.directory), filename)
                for filename in os.listdir(self.directory)
                if self.is_compatible(filename)
            ]

    def is_compatible(self, filename):
        """Check if a file is one of the compatible music files based on the extension"""
        file_extension = filename.split(".")[-1].lower()
        return file_extension in supported_formats

    def rename_music(self):
        """Rename all provided music"""
        for file in self.files:
            # Get the file extension
            filename, extension = os.path.splitext(file)

            # Read metadata
            track = TinyTag.get(file)

            # Show progress
            logging.info(f"Renaming track: '{track.artist}' - '{track.title}'.")

            # Use given format to set a new filename
            rename = []
            for metadata_field in self.format:
                if metadata_field == "track":
                    rename.append(f"{int(track.track):02}")
                else:
                    rename.append(getattr(track, metadata_field))
                rename.append(self.separator)
            rename.pop()

            # Replace forbidden characters
            rename = ''.join(rename)
            for char in invalid_characters:
                rename = rename.replace(char, self.replace)

            # Get absolute path and rename the audio file
            new_path = os.path.join(os.path.abspath(os.path.dirname(file)), rename + extension)
            os.rename(file, new_path)

            logging.info(f"Track: '{track.artist}' - '{track.title}' contained an illegal character; the character has been replaced with: '{self.replace}'.")
        logging.info("Renaming finished.")

def parse_args(argv, m_class):
    """Parse command line arguments"""
    try:
        opts, args = getopt.getopt(argv[2:], "s:rf:", ["separator=", "recursive", "format="])
    except getopt.GetoptError as error_mesg:
        logging.error(error_mesg)
        exit()

    # Handle command line arguments
    for opt, arg in opts:
        if opt in ['-s', '--separator']:
            m_class.separator = arg if check_separator(arg) else default_separator
        elif opt in ['-r', '--recursive']:
            m_class.recursive = True
        elif opt in ['-f', '--format']:
            m_class.format = arg.split(".")

    # Handle help and version options
    if '-h' in sys.argv or '--help' in sys.argv:
        print(help_text)
        exit()
    elif '-v' in sys.argv or '--version' in sys.argv:
        print(version_text)
        exit()

    # Set directory
    m_class.directory = sys.argv[1]
    
    if m_class.directory is None:
        logging.error("Please provide a music directory.")
        exit()

def check_separator(sep):
    if any(char in separator for char in invalid_characters):
        logging.warning(f"Given separator contains invalid filename symbols, defaulting to '{separator}'.\n")
        return False
    return True

def main():
    m_class = Musort()
    parse_args(sys.argv, m_class)
    m_class.get_files()
    m_class.display_settings()
    m_class.rename_music()

if __name__ == "__main__":
    main()
