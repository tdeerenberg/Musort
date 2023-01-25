#!/bin/bash
# Make sure to add ~/.local/bin to $PATH
pip3 install -r requirements.txt
cp src/musort.py ~/.local/bin/musort
echo "IF NOT DONE ALREADY, ADD '~/local/bin' TO $ PATH"