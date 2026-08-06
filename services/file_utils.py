import os
import shutil
import hashlib
import mimetypes

def file_exists(path):
    return os.path.isfile(path)

def folder_exists(path):
    return os.path.isdir(path)

def get_file_size(path):
    if not file_exists(path):
        return None
    return os.path.getsize(path)

def get_extension(path):
    return os.path.splitext(path)[1]

def get_mime_type(path):
    mime,_=mimetypes.guess_type(path)
    return mime

def copy_file(src,dst):
    shutil.copy2(src,dst)
    return True

def move_file(src,dst):
    shutil.move(src,dst)
    return True

def delete_file(path):
    os.remove(path)
    return True

def rename_file(src,dst):
    os.rename(src,dst)
    return True

def create_folder(path):
    os.makedirs(path,exist_ok=True)
    return True

def folder_size(folder):
    total=0
    for root,dirs,files in os.walk(folder):
        for file in files:
            filepath=os.path.join(root,file)
            total+=os.path.getsize(filepath)
    return total

def sha256(path):
    sha=hashlib.sha256()
    with open(path,"rb") as f:
        while True:
            chunk=f.read(4096)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()
