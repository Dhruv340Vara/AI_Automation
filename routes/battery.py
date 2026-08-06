from flask import Blueprint

from modules.battery import get_battery_info
from utils.response import success

battery_bp = Blueprint("battery", __name__)


@battery_bp.route("/battery")
def battery():
    return success(get_battery_info())
