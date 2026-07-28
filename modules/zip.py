import os
import zipfile

def zip_folder(source,destination):
    try:
        with zipfile.ZipFile(destination,"w",zipfile.ZIP_DEFLATED) as zipf:
            for root,dirs,files in os.walk(source):
                for file in files:
                    filepath=os.path.join(root,file)
                    arcname=os.path.relpath(filepath,source)
                    zipf.write(filepath,arcname)
        return {"success":True,"zip":destination}
    except Exception as e:
        return {"success":False,"error":str(e)}
