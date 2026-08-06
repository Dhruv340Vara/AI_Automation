from flask import Blueprint
from modules.download import get_download_file

download_bp=Blueprint("download",__name__)

@download_bp.route("/download/<filename>",methods=["GET"])
def download(filename):
    path=get_download_file(filename)
    if not path:
        return {"success":False,"error":"File not found"},404
    return send_file(path,as_attachment=True)
