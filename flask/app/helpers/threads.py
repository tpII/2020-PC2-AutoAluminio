import time
from datetime import datetime
import threading
import concurrent.futures


from app.helpers.vehicle import get_vehicle
from app.models.vehicle import Vehicle


def start_threads(app):
    get_vehicle().run()
    threading.Thread(target=save_status, args=(app, ), daemon=True).start()
    

def save_status(app):
    with app.app_context():
        max_version = Vehicle.max_version()
        if max_version:
            max_version = max_version + 1
        else:
            max_version = 1
            
        while True:
            vehicle_local = get_vehicle()
            Vehicle(version = max_version, 
                motor_1 = vehicle_local.get_speed_motor_1(),
                motor_2 = vehicle_local.get_speed_motor_2(),
                speed = vehicle_local.get_speed(),
                bumper_status = vehicle_local.get_parachoque_status(),
                created_at = datetime.today()
            ).save()
            time.sleep(1)
    