from flask import jsonify


def success(data=None, message="Success"):
    return jsonify({
        "success": True,
        "message": message,
        "data": data
    })


def error(message="Error"):
    return jsonify({
        "success": False,
        "message": message
    })
