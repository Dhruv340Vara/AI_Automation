import os

ROOT_DIR="/storage/emulated/0/AI_Automation"

UPLOADS_DIR=os.path.join(ROOT_DIR,"Uploads")
DOWNLOADS_DIR=os.path.join(ROOT_DIR,"Downloads")
PHOTOS_DIR=os.path.join(ROOT_DIR,"Photos")
VIDEOS_DIR=os.path.join(ROOT_DIR,"Videos")
DOCUMENTS_DIR=os.path.join(ROOT_DIR,"Documents")
BACKUPS_DIR=os.path.join(ROOT_DIR,"Backups")
TEMP_DIR=os.path.join(ROOT_DIR,"Temp")
RECYCLE_BIN_DIR=os.path.join(ROOT_DIR,"RecycleBin")
LOGS_DIR=os.path.join(ROOT_DIR,"Logs")
AI_DATA_DIR=os.path.join(ROOT_DIR,"AI")

ALL_FOLDERS=[
ROOT_DIR,
UPLOADS_DIR,
DOWNLOADS_DIR,
PHOTOS_DIR,
VIDEOS_DIR,
DOCUMENTS_DIR,
BACKUPS_DIR,
TEMP_DIR,
RECYCLE_BIN_DIR,
LOGS_DIR,
AI_DATA_DIR
]

def initialize_storage():
    for folder in ALL_FOLDERS:
        os.makedirs(folder,exist_ok=True)
    return True

def storage_exists():
    return os.path.exists(ROOT_DIR)

def get_root():
    return ROOT_DIR

def get_upload_path():
    return UPLOADS_DIR

def get_download_path():
    return DOWNLOADS_DIR

def get_photo_path():
    return PHOTOS_DIR

def get_backup_path():
    return BACKUPS_DIR

def get_temp_path():
    return TEMP_DIR

def get_recycle_path():
    return RECYCLE_BIN_DIR
