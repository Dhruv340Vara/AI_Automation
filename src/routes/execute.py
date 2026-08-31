from flask import Blueprint, request
from automation.actions.action_handler import handle_action
from automation.utils.response import success_response, error_response

execute_bp = Blueprint("execute", __name__)

@execute_bp.route("/execute", methods=["POST"])
def execute():
    try:
        data = request.get_json(silent=True) or {}

        action = data.get("action")
        payload = data.get("data", {})

        if not action:
            return error_response("Action is required")

        result = handle_action(action, payload)

        if "error" in result:
            return error_response(result["error"])

        return success_response(result.get("message", "Done"))

    except Exception as e:
        return error_response(str(e))