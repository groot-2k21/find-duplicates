import os
import hashlib
from sys import argv

if len(argv) <= 1:
    exit

argv.pop(0)
for root_dir in argv:

    move_dir = os.path.join(root_dir, "ОТСЕВ")

    files = os.listdir(root_dir)
    hashlist = []

    try:
        os.mkdir(move_dir)
    except FileExistsError:
        print("Директория существует")


tree = os.walk("/home/groot/Pictures/GDrive/")

for path, dirs, files in tree:
    if not len(files):
        continue
    
    for f in files:
        fr = os.path.join(path, f)

        if os.path.isfile(fr):
            f_hash = hashlib.md5(open(fr, 'rb').read()).hexdigest()
        
        if f_hash not in hashlist:
            hashlist.append(f_hash)
        else:
            print(fr)
            os.replace(fr, os.path.join(move_dir, f))