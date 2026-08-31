# automation/core/action_handler.py

from modules.torch import torch_on, torch_off

def handle_action(action, data=None):
    action = action.lower()

    if action == "torch_on":
        return {"message": torch_on()}

    elif action == "torch_off":
        return {"message": torch_off()}

    else:
        return {"error": f"Unknown action: {action}"}
