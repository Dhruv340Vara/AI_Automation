from flask import Blueprint, request

from modules.notification import notify
from utils.response import success

notification_bp = Blueprint("notification", __name__)


@notification_bp.route("/notification", methods=["POST"])
def notification():

    data = request.get_json(silent=True) or {}

    title = data.get("title", "AI Automation")

    content = data.get("content", "")

    return success(
        notify(title, content)
    )
