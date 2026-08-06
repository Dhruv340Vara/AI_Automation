from flask import Blueprint

from modules.storage import get_storage_info
from utils.response import success

storage_bp = Blueprint("storage", __name__)


@storage_bp.route("/storage")
def storage():
    return success(get_storage_info())
