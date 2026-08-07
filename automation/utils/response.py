def success_response(message="", data=None):
    return {
        "success": True,
        "message": message,
        "data": data or {}
    }

def error_response(message="Error", data=None):
    return {
        "success": False,
        "message": message,
        "data": data or {}
    }
