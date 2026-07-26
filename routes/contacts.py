from flask import Blueprint

from modules.contacts import get_contacts
from utils.response import success

contacts_bp = Blueprint("contacts", __name__)


@contacts_bp.route("/contacts", methods=["GET"])
def contacts():
    return success(get_contacts())
