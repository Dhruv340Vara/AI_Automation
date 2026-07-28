from flask import Blueprint,request
from modules.delete_request import request_delete
from utils.response import success

delete_request_bp=Blueprint("delete_request",__name__)

@delete_request_bp.route("/delete/request",methods=["POST"])
def delete_request():
    data=request.get_json(silent=True) or {}
    path=data.get("path")
    if not path:
        return success({"error":"path required"})
    return success(request_delete(path))
