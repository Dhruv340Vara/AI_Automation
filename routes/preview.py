from flask import Blueprint,request
from modules.preview import preview_file
from utils.response import success

preview_bp=Blueprint("preview",__name__)

@preview_bp.route("/preview",methods=["POST"])
def preview():
    data=request.get_json(silent=True) or {}
    path=data.get("path")
    if not path:
        return success({"error":"path required"})
    return success(preview_file(path))
