import os
import shutil
from services.storage_manager import get_upload_path

def upload_file(source):
    try:
        if not os.path.isfile(source):
            return {"success":False,"error":"File not found"}
        destination=os.path.join(get_upload_path(),os.path.basename(source))
        shutil.copy2(source,destination)
        return {"success":True,"source":source,"destination":destination}
    except Exception as e:
        return {"success":False,"error":str(e)}
