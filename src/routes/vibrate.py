from flask import Blueprint, request

from modules.vibrate import vibrate
from utils.response import success

vibrate_bp = Blueprint("vibrate", __name__)


@vibrate_bp.route("/vibrate", methods=["POST"])
def vibrate_api():

    data = request.get_json(silent=True) or {}

    duration = data.get("duration", 500)

    return success(vibrate(duration))
