from flask import render_template
from app.helpers import handler
from app.controller import main 
from app.controller import vehicle

def set_routes(app):

    app.add_url_rule("/", "home", main.index)
    
    # api vehiculo
    app.add_url_rule("/api/vehicle/status", "api_vehicle_status", vehicle.status)
    app.add_url_rule("/api/vehicle/historical", "api_vehicle_historical", vehicle.historical)
    app.add_url_rule("/api/vehicle/control/<int:code>", "api_vehicle_control",vehicle.control, methods=["POST"])

    app.add_url_rule("/api/vehicle/export", "api_vehicle_export", vehicle.export)
    
    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    