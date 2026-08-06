from flask import Blueprint, request

from modules.torch import torch_on, torch_off
from utils.response import success

torch_bp = Blueprint("torch", __name__)


@torch_bp.route("/torch", methods=["POST"])
def torch():

    data = request.get_json(silent=True) or {}

    action = data.get("action", "").lower()

    if action == "on":
        return success(torch_on())

    elif action == "off":
        return success(torch_off())

    return success({
        "error": "Use action = on/off"
    })
