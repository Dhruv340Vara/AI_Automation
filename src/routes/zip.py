from flask import Blueprint,request
from modules.zip import zip_folder
from utils.response import success

zip_bp=Blueprint("zip",__name__)

@zip_bp.route("/zip",methods=["POST"])
def zip_api():
    data=request.get_json(silent=True) or {}
    source=data.get("source")
    destination=data.get("destination")
    if not source or not destination:
        return success({"error":"source and destination required"})
    return success(zip_folder(source,destination))
