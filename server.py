from routes.volume import volume_bp
from routes.clipboard import clipboard_bp
from flask import Flask, jsonify
from routes.wifi import wifi_bp
from routes.battery import battery_bp
from routes.storage import storage_bp
from routes.device import device_bp

app = Flask(__name__)

app.register_blueprint(battery_bp)
app.register_blueprint(device_bp)
app.register_blueprint(volume_bp)
app.register_blueprint(wifi_bp)
app.register_blueprint(clipboard_bp)
app.register_blueprint(storage_bp)

@app.route("/")
def home():
    return jsonify({
        "project": "AI Automation Server",
        "version": "1.0",
        "status": "Running"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
