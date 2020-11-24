from flask import render_template
from app.helpers import handler
from app.controller import main 
from app.controller import vehicle

def set_routes(app):

    
    # Ruta para el Home
    app.add_url_rule("/", "index", main.index)
    app.add_url_rule("/0", "index_stop", main.stop)
    app.add_url_rule("/1", "index_up", main.up)
    app.add_url_rule("/2", "index_down", main.down)
    app.add_url_rule("/3", "index_right", main.right)
    app.add_url_rule("/4", "index_left", main.left)

    # api vehiculo
    app.add_url_rule("/api/vehicle/status", "api_vehicle_status", vehicle.status)
    app.add_url_rule("/api/vehicle/historical", "api_vehicle_historical", vehicle.historical)
    app.add_url_rule("/api/vehicle/control/<int:code>", "api_vehicle_control",vehicle.control, methods=["POST"])

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    