from flask import Blueprint, request

from modules.volume import get_volume, set_volume
from utils.response import success

volume_bp = Blueprint("volume", __name__)


@volume_bp.route("/volume", methods=["GET"])
def volume_get():
    return success(get_volume())


@volume_bp.route("/volume", methods=["POST"])
def volume_set():

    data = request.get_json()

    stream = data.get("stream", "music")

    volume = data.get("volume", 5)

    return success(set_volume(stream, volume))
