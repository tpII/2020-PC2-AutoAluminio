from datetime import datetime
from flask import  abort, jsonify
from app.helpers.vehicle import get_vehicle
from app.models.vehicle import Vehicle

def status():
    vehicle = get_vehicle()
    response = {
                "data":
                {
                    "position_x": vehicle.get_position_x(),
                    "position_y": vehicle.get_position_y(),
                    "bumper_status": vehicle.get_parachoque_status(),
                    "speed": vehicle.get_speed(),
                    "speed_motor_1": vehicle.get_speed_motor_1(),
                    "speed_motor_2": vehicle.get_speed_motor_2(),
                    "datetime": datetime.today().strftime("%d/%m/%Y-%H:%M:%S")
                }
            }
    return jsonify(response)

def historical():
    array_json = []
    regs = Vehicle.last(15)
    for veh in regs:
        array_json.append({
            'version': veh.version,
            'motor_1': veh.motor_1,
            'motor_2': veh.motor_2,
            'speed':veh.speed,
            'bumper_status': veh.bumper_status,
            'created_at': veh.created_at.strftime("%d/%m/%Y-%H:%M:%S")
        })
    return jsonify({'data': array_json})

def export():
    array_json = []
    regs = Vehicle.all_max_version()
    for veh in regs:
        array_json.append({
            'version': veh.version,
            'motor_1': veh.motor_1,
            'motor_2': veh.motor_2,
            'speed':veh.speed,
            'bumper_status': veh.bumper_status,
            'created_at': veh.created_at.strftime("%d/%m/%Y-%H:%M:%S")
        })

    return jsonify( {"data": array_json})
    
    
def control(code):
    if code == 0:
        get_vehicle().stop()
        return jsonify({"data": "success stop"})
    if code == 1:
        get_vehicle().up()
        return jsonify({"data": "success up"})
    if code == 2:
        get_vehicle().down()
        return jsonify({"data": "success down"})
    if code == 3:
        get_vehicle().right()
        return jsonify({"data": "success right"})
    if code == 4:
        get_vehicle().left()
        return jsonify({"data": "success left"})
    return abort(400)