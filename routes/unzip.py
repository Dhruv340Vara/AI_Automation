from flask import Blueprint,request
from modules.unzip import unzip_file
from utils.response import success

unzip_bp=Blueprint("unzip",__name__)

@unzip_bp.route("/unzip",methods=["POST"])
def unzip():
    data=request.get_json(silent=True) or {}
    source=data.get("source")
    destination=data.get("destination")
    if not source or not destination:
        return success({"error":"source and destination required"})
    return success(unzip_file(source,destination))
