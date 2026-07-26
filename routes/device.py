from flask import Blueprint

from modules.device import get_device_info
from utils.response import success

device_bp = Blueprint("device", __name__)


@device_bp.route("/device")
def device():
    return success(get_device_info())
