from flask import Blueprint, request

from modules.sms import send_sms
from utils.response import success

sms_bp = Blueprint("sms", __name__)


@sms_bp.route("/sms", methods=["POST"])
def sms():

    data = request.get_json(silent=True) or {}

    number = data.get("number")

    message = data.get("message")

    if not number or not message:

        return success({
            "error": "number and message required"
        })

    return success(
        send_sms(number, message)
    )
