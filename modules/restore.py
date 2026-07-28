import os
import json
import shutil
from services.storage_manager import get_recycle_files_path,get_recycle_metadata_path

def restore_file(filename):
    try:
        recycle=os.path.join(get_recycle_files_path(),filename)
        metadata=os.path.join(get_recycle_metadata_path(),filename+".json")
        if not os.path.isfile(recycle):
            return {"success":False,"error":"File not found"}
        if not os.path.isfile(metadata):
            return {"success":False,"error":"Metadata missing"}
        with open(metadata,"r") as f:
            info=json.load(f)
        destination=info["original_path"]
        os.makedirs(os.path.dirname(destination),exist_ok=True)
        shutil.move(recycle,destination)
        os.remove(metadata)
        return {"success":True,"restore":destination}
    except Exception as e:
        return {"success":False,"error":str(e)}
