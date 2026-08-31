from flask import Blueprint, request

from modules.tts import speak
from utils.response import success

tts_bp = Blueprint("tts", __name__)


@tts_bp.route("/tts", methods=["POST"])
def tts():

    data = request.get_json(silent=True) or {}

    text = data.get("text", "")

    return success(speak(text))
