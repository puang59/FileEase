#!/usr/bin/env python3

# source - https://github.com/puang59/fileOrganizer

import os
import shutil

files = os.listdir()

for file in files:
    # organize images
    imageExts = ['.jpg', '.jpeg', '.png', '.gif']
    filename, extension = os.path.splitext(file)
    if extension.lower() in imageExts:
        shutil.move(file, os.path.join('Media/images', file))

    # organize screenshots
    if file.startswith("Screenshot"):
        shutil.move(file, "Media/screenshots/" + file)

    # organize videos
    if file.endswith(".mp4") or file.startswith("Screen Recording"):
        shutil.move(file, "Media/videos" + file)

    # other
    miscExts = ['.zip', '.psd', '.webp', '.dmg', '.pdf']
    if extension.lower() in miscExts:
        shutil.move(file, os.path.join('Media/misc', file))
