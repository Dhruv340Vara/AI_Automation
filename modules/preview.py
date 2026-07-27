import os
from services.file_utils import get_file_size,get_extension,get_mime_type

def preview_file(path):
    try:
        if not os.path.isfile(path):
            return {"success":False,"error":"File not found"}
        return {
            "success":True,
            "name":os.path.basename(path),
            "path":path,
            "size":get_file_size(path),
            "extension":get_extension(path),
            "mime":get_mime_type(path)
        }
    except Exception as e:
        return {"success":False,"error":str(e)}
