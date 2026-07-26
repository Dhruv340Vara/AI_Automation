from flask import Blueprint

from modules.location import get_location
from utils.response import success

location_bp = Blueprint("location", __name__)


@location_bp.route("/location", methods=["GET"])
def location():

    return success(get_location())
