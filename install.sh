#!/bin/bash
#
# Musort - Install and Upgrade Script
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

# Define paths
install_path=~/.local/bin
script_name=musort
script_path=src/musort.py
script_config=src/config.py
script_tinytag=src/tinytag.py
script_variables=src/variables.py

# Check if script already exists
if [ -e "$install_path/$script_name" ]; then
    read -p "Musort is already installed. Do you want to overwrite it with the new version? (y/n): " response
    if [[ $response =~ ^[Yy]$ ]]; then
        echo "Updating Musort..."
        cp "$script_path" "$install_path/$script_name"
        cp "$script_config" "$install_path/"
        cp "$script_tinytag" "$install_path/"
        cp "$script_variables" "$install_path/"
        echo "Musort updated successfully!"
    else
        echo "Upgrade canceled. Musort remains unchanged."
    fi
else
    # Install Musort
    cp "$script_path" "$install_path/$script_name"
    cp "$script_config" "$install_path/"
    cp "$script_tinytag" "$install_path/"
    cp "$script_variables" "$install_path/"
    echo "Musort installed successfully!"
fi

echo "If not done already, add '$install_path' to \$PATH"