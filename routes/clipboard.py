from flask import Blueprint, request

from modules.clipboard import get_clipboard, set_clipboard
from utils.response import success

clipboard_bp = Blueprint("clipboard", __name__)


@clipboard_bp.route("/clipboard", methods=["GET"])
def clipboard_get():
    return success(get_clipboard())


@clipboard_bp.route("/clipboard", methods=["POST"])
def clipboard_set():

    data = request.get_json()

    text = data.get("text", "")

    return success(set_clipboard(text))
