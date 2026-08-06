from flask import Blueprint,request
from modules.permissions import get_permissions,set_permissions
from utils.response import success

permissions_bp=Blueprint("permissions",__name__)

@permissions_bp.route("/permissions",methods=["GET"])
def permissions_get():
    path=request.args.get("path")
    if not path:
        return success({"error":"path required"})
    return success(get_permissions(path))

@permissions_bp.route("/permissions",methods=["POST"])
def permissions_set():
    data=request.get_json(silent=True) or {}
    path=data.get("path")
    permission=data.get("permission")
    if not path or not permission:
        return success({"error":"path and permission required"})
    return success(set_permissions(path,permission))
