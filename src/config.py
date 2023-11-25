#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


#
# These are the default settings of Musort.
# Default settings are used when no parameters are given.
# The default settings may be changed to your liking.
#

# Change separator between the naming format
separator = "."

# Toggle recursively renaming though subdirectories
recursive = False

# Format for renaming music files
name_format = "track.title"

# Replacement for illegal characters
forbidden_char_replace = "_"