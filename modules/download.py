import os
from flask import send_file
from services.storage_manager import get_download_path

def get_download_file(filename):
    path=os.path.join(get_download_path(),filename)
    if not os.path.isfile(path):
        return None
    return path
