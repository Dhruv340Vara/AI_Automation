from flask import Blueprint,request
from modules.permanent_delete import permanent_delete
from utils.response import success

delete_bp=Blueprint("delete",__name__)

@delete_bp.route("/delete/confirm",methods=["POST"])
def delete():
    data=request.get_json(silent=True) or {}
    token=data.get("token")
    if not token:
        return success({"error":"token required"})
    return success(permanent_delete(token))
