from routes.delete_request import delete_request_bp
from services.storage_manager import initialize_storage
from routes.recycle import recycle_bp
from routes.restore import restore_bp
from routes.permanent_delete import delete_bp
from routes.zip import zip_bp
from routes.unzip import unzip_bp
from routes.permissions import permissions_bp
from routes.upload import upload_bp
from routes.download import download_bp
from routes.preview import preview_bp
from routes.contacts import contacts_bp
from routes.camera import camera_bp
from routes.location import location_bp
from routes.sms import sms_bp
from routes.torch import torch_bp
from routes.tts import tts_bp
from routes.notification import notification_bp
from routes.vibrate import vibrate_bp
from routes.volume import volume_bp
from routes.clipboard import clipboard_bp
from flask import Flask, jsonify
from routes.wifi import wifi_bp
from routes.battery import battery_bp
from routes.storage import storage_bp
from routes.device import device_bp

app = Flask(__name__)

initialize_storage()
app.register_blueprint(location_bp)
app.register_blueprint(sms_bp)
app.register_blueprint(battery_bp)
app.register_blueprint(recycle_bp)
app.register_blueprint(restore_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(download_bp)
app.register_blueprint(delete_request_bp)
app.register_blueprint(zip_bp)
app.register_blueprint(unzip_bp)
app.register_blueprint(permissions_bp)
app.register_blueprint(preview_bp)
app.register_blueprint(contacts_bp)
app.register_blueprint(camera_bp)
app.register_blueprint(torch_bp)
app.register_blueprint(tts_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(device_bp)
app.register_blueprint(volume_bp)
app.register_blueprint(vibrate_bp)
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
