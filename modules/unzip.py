import zipfile

def unzip_file(source,destination):
    try:
        with zipfile.ZipFile(source,"r") as zipf:
            zipf.extractall(destination)
        return {"success":True,"destination":destination}
    except Exception as e:
        return {"success":False,"error":str(e)}

