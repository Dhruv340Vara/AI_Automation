from flask import Blueprint,request
from modules.recycle import recycle_file
from utils.response import success

recycle_bp=Blueprint("recycle",__name__)

@recycle_bp.route("/recycle",methods=["POST"])
def recycle():
    data=request.get_json(silent=True) or {}
    path=data.get("path")
    if not path:
        return success({"error":"path required"})
    return success(recycle_file(path))
