#!/bin/sh

echo Installing Homebrew, a package manager for MacOS...
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo Done!

echo Changing permissions inside /usr/local so that homebrew can access these files..
sudo chown -R $(whoami) $(brew --prefix)/*
echo Done!

echo Installing Python3
brew install python3
echo Done!

echo Installing ffmpeg
brew install ffmpeg

echo Installing UlozitTutoPiesen
python3 -m pip install UlozitTutoPiesen --no-cache-dir --ignore-installed
echo Done!

echo UlozitTutoPiesen has been installed! You can run the script by running 'utp' on a terminal window.
