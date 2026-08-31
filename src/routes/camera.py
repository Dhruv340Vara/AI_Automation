from flask import Blueprint, request

from modules.camera import capture_photo
from utils.response import success

camera_bp = Blueprint("camera", __name__)


@camera_bp.route("/camera", methods=["POST"])
def camera():

    data = request.get_json(silent=True) or {}

    camera = str(data.get("camera", 0))

    return success(capture_photo(camera))
