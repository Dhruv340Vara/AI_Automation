from modules.torch import torch_on, torch_off

def handle_action(action, data=None):

    if action == "torch_on":
        torch_on()
        return {"message": "Torch turned ON"}

    elif action == "torch_off":
        torch_off()
        return {"message": "Torch turned OFF"}

    else:
        return {"error": "Unknown action"}
