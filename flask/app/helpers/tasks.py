import time
from datetime import datetime

from app.models.vehicle import Vehicle
from app.helpers.vehicle import get_vehicle

def threaded_task(app):
    get_vehicle().run()

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
                created_at = datetime.today().replace(microsecond=0)
        ).save()
        time.sleep(1)

    