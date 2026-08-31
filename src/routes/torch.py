from flask import Blueprint, request
from modules.torch import torch_on, torch_off
from automation.utils.response import success_response, error_response

torch_bp = Blueprint("torch", __name__)

@torch_bp.route("/torch", methods=["POST"])
def torch():
    try:
        data = request.get_json(silent=True) or {}
        action = data.get("action", "").lower()

        if action == "on":
            torch_on()
            return success_response("Torch turned ON")

        elif action == "off":
            torch_off()
            return success_response("Torch turned OFF")

        else:
            return error_response("Use action = on/off")

    except Exception as e:
        return error_response(str(e))