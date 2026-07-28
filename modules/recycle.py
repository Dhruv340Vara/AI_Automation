import os
import json
import shutil
from datetime import datetime
from services.storage_manager import get_recycle_files_path,get_recycle_metadata_path
from services.file_utils import get_file_size,get_mime_type,sha256

def recycle_file(path):
    try:
        if not os.path.exists(path):
            return {"success":False,"error":"File not found"}
        filename=os.path.basename(path)
        recycle=os.path.join(get_recycle_files_path(),filename)
        metadata=os.path.join(get_recycle_metadata_path(),filename+".json")
        shutil.move(path,recycle)
        info={
            "filename":filename,
            "original_path":path,
            "deleted_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "size":get_file_size(recycle),
            "mime":get_mime_type(recycle),
            "sha256":sha256(recycle)
        }
        with open(metadata,"w") as f:
            json.dump(info,f,indent=4)
        return {"success":True,"file":recycle}
    except Exception as e:
        return {"success":False,"error":str(e)}
