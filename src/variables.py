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

version_text = "Musort v1.0 (C) tdeerenberg"
supported_formats = ["flac", "mp3", "mp2", "mp1", "opus", "ogg", "wma"]
invalid_characters = ["\\", "/", "|", "*", "<", ">", '"', "'", "?"]
default_separator = '_'
help_text = \
"""Musort (c) 2023 tdeerenberg (github.com/tdeerenberg)

DESCRIPTION:
A command-line tool for effortlessly organizing and renaming your music files based on metadata

USAGE:
musort [DIRECTORY] [OPTIONAL_PARAMETERS]
    
USAGE EXAMPLES:
    musort ~/music
    musort /local/music -f disc.artist.title.album -r
    musort ~/my_music -s _ -r
    
OPTIONAL OPTIONS:
-h, --help           Show the help menu
-f, --format         set the naming convention (see 'NAMING CONVENTION:' below)
-s, --separator      Set the separator for the filename (ex. '-s .' -> 01.track.flac and '-s -' -> 01-track.mp3)
                     Default separator '_' will be used if none is given
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
year            year or date as string"""