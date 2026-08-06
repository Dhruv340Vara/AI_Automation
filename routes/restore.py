from flask import Blueprint,request
from modules.restore import restore_file
from utils.response import success

restore_bp=Blueprint("restore",__name__)

@restore_bp.route("/restore",methods=["POST"])
def restore():
    data=request.get_json(silent=True) or {}
    filename=data.get("filename")
    if not filename:
        return success({"error":"filename required"})
    return success(restore_file(filename))
