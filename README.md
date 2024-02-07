https://github.com/tdeerenberg/Musort/assets/113618658/38ce8dc2-7a5f-4edd-9d56-11408d1d56dd

# Musort
Musort: Effortlessly organize your music library with this Python3 program. Rename selected music/audio files in a folder using a customizable naming convention based on metadata (ID3) from the audio files. Ensure accurate metadata by using popular tools like MusicBrainz Picard, Beets, or EasyTAG before running Musort. Simplify your music organization and enhance file names for a more enjoyable library experience.

## Features

* Rename many audio files at once
* Rename audio files in subdirectories as well (recursive)
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
**Make sure to install these programs to be able to run Musort**
- [Python3](https://www.python.org/)
- [Docker (Optional)](https://docker.com)

The Python3 library TinyTag is also used, but is already included in this repository. Therefore, there is no need to install TinyTag for only this project.

## Installation and Usage

### Method 1: Run installation script (Unix/Linux based OS only)

The installation script will move the python program to `~/.local/bin`. The installation directory can be changed in the `install.sh` script. **Note: The installation directory should be added to $PATH**
``` Bash
git clone https://github.com/tdeerenberg/Musort.git
cd Musort
chmod +x install.sh
./install.sh
```
After that, simply use the command `musort` to use the program.
<hr>

### Method 2: Clone repo and run manually (All Operating Systems)

Clone the repository and run the Python program
``` Bash
git clone https://github.com/tdeerenberg/Musort.git
cd Musort
pip install requirements.txt
```
After that, run the program with `python3 musort.py`.
<hr>

### Method 3: Docker installation

``` Bash
git clone https://github.com/tdeerenberg/Musort.git
cd Musort
docker build -t musort .
```
After the Docker installation/build is complete, Musort can be run with: 

`docker run --name musort --rm -v "[music_directory_host]:[music_directory_container]" -it musort [music_directory_container]`

The music folder must be mounted to the Docker container, therefore the `-v` option must be used to mount the directory.

An example of running Musort in Docker, using `/home/user/music` as music folder:

`docker run --name musort --rm -v '/home/user/music:/music' -it musort /music`

## Manual with options and arguments (`musort --help`)
```
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
year            year or date as string
```

## Possible features to add
* Rename single file
* Other installation methods (e.g. via AUR)
* Open for suggestions!
* Feel free to open a pull request or issue!

## Authors

- [@tdeerenberg](https://github.com/tdeerenberg)

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. 
