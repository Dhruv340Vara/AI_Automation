from flask import Blueprint

from modules.wifi import get_wifi_info
from utils.response import success

wifi_bp = Blueprint("wifi", __name__)


@wifi_bp.route("/wifi")
def wifi():
    return success(get_wifi_info())
