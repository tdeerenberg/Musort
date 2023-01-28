#!/usr/bin/env python

# Licensed under GPLv3
# Copyright (C) 2023 tdeerenberg

from tinytag import TinyTag
import os
import sys, getopt
import logging

supported_formats = ["flac", "mp3", "mp2", "mp1", "opus", "ogg", "wma"]

version = "Musort v0.1 (c) tdeerenberg"
help=\
"""Musort (c) 2023 tdeerenberg (github.com/tdeerenberg)

DESCRIPTION:
A Python3 program that renames all selected music/audio files in a folder with a specified naming convention

USAGE:
musort [DIRECTORY] [NAMING_CONVENTION] [OPTIONAL_OPTIONS]...

    USAGE EXAMPLES:
    musort ~/music track.title.year -s _ -r
    musort /local/music disc.artist.title.album -r
    musort ~/my_music track.title

OPTIONAL OPTIONS:
-h, --help           Show the help menu
-s, --separator      Set the separator for the filename (ex. '-s .' -> 01.track.flac and '-s -' -> 01-track.mp3)
                     Default separator ( . ) will be used if none is given
-r, --recursive      Rename files in subdirectories as well
-v, --version        Prints the version number

NAMING CONVENTION:
FORMAT_OPTION.FORMAT_OPTION...      The amount of format options does not matter.
                                    It can be one, two, three, even all of them.
                                    (See FORMAT OPTIONS below for all options)

FORMAT OPTIONS:
album           album as string
albumartist     album artist as string
artist          artist name as string
audio_offset    number of bytes before audio data begins
bitdepth        bit depth for lossless audio
bitrate         bitrate in kBits/s
comment         file comment as string
composer        composer as string 
disc            disc number
disc_total      the total number of discs
duration        duration of the song in seconds
filesize        file size in bytes
genre           genre as string
samplerate      samples per second
title           title of the song
track           track number as string
track_total     total number of tracks as string
year            year or date as string

SUPPORTED AUDIO FORMATS:
MP3/MP2/MP1 (ID3 v1, v1.1, v2.2, v2.3+)
Wave/RIFF
OGG
OPUS
FLAC
WMA
MP4/M4A/M4B/M4R/M4V/ALAC/AAX/AAXC"""

class Music:
    def get_files(self, directory):
        """Scans the set directory for compatible audio files"""
        self.files = list(map(lambda x: os.path.join(os.path.abspath(directory), x),os.listdir(directory)))

    def get_files_recursive(self, directory):
        """Scans the set directory with subdirectory for compatible audio files"""
        files = []
        for a, b, c in os.walk(directory):
            for d in c:
                files.append(os.path.join(a,d))
        self.files = files
        
    def get_compatible(self):
        music = []
        for file in self.files:
            file_extension = file.split(".")[-1]

            if file_extension in supported_formats:
                music.append(file)

        self.compatible = music

    def set_separator(self, sep):
        """Sets the separator for naming the audio files
        (ex. 01-songname.mp3 or 01.songname.flac)"""
        self.separator = sep

    def set_format(self, val):
        """Sets the naming convention of the audio files
        (ex. title-artist or artist-track-title)"""
        self.format = val.split(".")

    # Rename files
    def rename_music(self):
        """Rename all compatible music files"""

        """Get the file extension (ex. .flac, .mp3, etc)"""
        for file in self.compatible:
            ext = file.split(".")
            ext = "." + ext[-1]

            """Let TinyTag module read the audio file"""
            track = TinyTag.get(file)

            """Print the progress (Current track)"""
            logging.info(f"Current track: '{track.artist}' - '{track.title}'")
            rename = []

            """Uses the given format to set new filename"""
            for f in self.format:

                if f == "track":
                    rename.append(f"{int(track.track):02}")
                else:
                    """getattr gets attribute in track with name f"""
                    rename.append(getattr(track, f))

                rename.append(self.separator)
            rename.pop()
            rename = ''.join(rename)+ext
            """Replacing forbidden path characters in UNIX and Windows with underscores"""
            for forbidden_character in ['\\', '/', '|', '*', '<', '>', '"', '?']:
                if forbidden_character in rename:
                    logging.warning(f"Track '{track.artist}' - '{track.title}': found the forbidden path character ({forbidden_character}) in the new file name, replaced symbol with underscore")
                    rename = rename.replace(forbidden_character, "_")

            """Get the absolute path and rename the audio file"""
            dst = os.path.join(os.path.abspath(os.path.dirname(file)), rename)
            os.rename(file, dst)
        logging.info("Actions finished")

def main():
    level = logging.DEBUG
    logging.basicConfig(level=level, format='[%(levelname)s] %(asctime)s - %(message)s')
    """Runs the whole program"""
    argv = sys.argv[3:]
    try:
        opts, args = getopt.getopt(argv, "s:r", ["sep=", "recursive="])
    except getopt.GetoptError as err:
        logging.error(err)
        exit()

    music = Music()
    for opt, arg in opts:
        if opt in ['-s', '--separator']:
            logging.info(f"Using {arg} as separator")
            music.set_separator(arg)
        if opt in ['-r', '--recursive']:
            logging.info("Running recursively")
            music.get_files_recursive(sys.argv[1])
            music.get_compatible()

    if sys.argv[1] == "-h" or sys.argv[1] == '--help':
        print(help)
        exit()
    if sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print(version)
        exit()
    try:
        music.compatible
    except:
        logging.info("Running not recursively")
        music.get_files(sys.argv[1])
        music.get_compatible()
    try:
        music.separator
    except:
        logging.info("Using default separator")
        music.set_separator(".")

    music.set_format(sys.argv[2])
    music.rename_music()

if __name__ == "__main__":
    main()
