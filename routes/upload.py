from flask import Blueprint,request
from modules.upload import upload_file
from utils.response import success

upload_bp=Blueprint("upload",__name__)

@upload_bp.route("/upload",methods=["POST"])
def upload():
    data=request.get_json(silent=True) or {}
    source=data.get("source")
    if not source:
        return success({"error":"source required"})
    return success(upload_file(source))
