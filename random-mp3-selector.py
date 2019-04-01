import os
import shutil
import random

# source directory for files to copy from
source_dir = "E:\\_Temp\\Music"
# target directory for files to copy to
target_dir = "C:\\test\\to"  

 # empty list for collecting files
source_files = []  

# walk through directory tree and find files only
for dirpath, dirnames, filenames in os.walk(source_dir):
    for file in filenames:
        if file.endswith(".mp3"):
            source_files.append(os.path.join(dirpath, file))

# select 300 files randomly               
choices = random.sample(source_files, 300)
print(choices)

# copy files to target directory
for files in choices:
    shutil.copy(files, target_dir)