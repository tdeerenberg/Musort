https://user-images.githubusercontent.com/113618658/214463785-49c419e9-c959-4849-91d2-f3407ecaa73d.mp4
# Musort

A Python3 program that renames all selected music/audio files in a folder with a specified naming convention. Names are generated from the metadata (ID3) from the audio files. Before using this program, use a metadata editor like MusicBrainz Picard, Beets or EasyTAG to add the correct metadata to the audio files.

## Features

* Rename many audio files at once
* Rename all files in subdirectories as well (recursive)
* Choose the naming convention (ex. track.title.flac or artist.track.year.mp3)
* Give a separator for the naming of the file (ex. track.title.flac or track_title.flac)
* Works on all systems that can run Python
* Supported audio formats  
  * MP3/MP2/MP1 (ID3 v1, v1.1, v2.2, v2.3+)
  * Wave/RIFF
  * OGG
  * OPUS
  * FLAC
  * WMA
  * MP4/M4A/M4B/M4R/M4V/ALAC/AAX/AAXC
  * AIFF/AIFF-C

## Dependencies
**Note: When using the install script, TinyTag will be automatically installed**
- [Python3](https://www.python.org/)
- [TinyTag](https://pypi.org/project/tinytag/) (Installable from Python Package Index)
## Installation and Usage

### Method 1: Run installation script (Unix/Linux based OS only)
The installation script will move the python program to `~/.local/bin`. Make sure that `~/.local/bin` exists and that is added to $PATH.
``` Bash
git clone https://github.com/tdeerenberg/Musort.git
cd Musort.git
chmod +x install.sh
./install.sh
```
After that, simply use the command `musort` to use the program.
### Method 2: Clone repo and run manually (All Operating Systems)
Clone the repository and run the Python program
``` Bash
git clone https://github.com/tdeerenberg/Musort.git
cd Musort
pip install requirements.txt
```
After that, run the program with `python3 musort.py`.
## Manual (options and arguments) `musort --help`
```
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
```
## Authors

- [@tdeerenberg](https://www.github.com/tdeerenberg)

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. 
