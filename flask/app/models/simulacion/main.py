import logging
import threading
import time
import concurrent.futures
import queue
import msvcrt

from modelos.servo import Servomotor
from modelos.parachoque import Parachoque
#from modelos.vehicle import Vehicle
from modelos.vehicle_oo2 import Vehicle
from datetime import datetime
def main():

    vehicle = Vehicle()
    vehicle.run()

    done = False
    # Se ejecuta el hilo principal
    while True:

        time_now = datetime.now().strftime("%H:%M:%S")
        print(f"[{time_now}] Posición del vehiculo: ({vehicle.get_position_x()},{vehicle.get_position_y()}) Motores ({vehicle.get_speed_motor_1()},{vehicle.get_speed_motor_2()}) - Parachoque {vehicle.get_parachoque_status()} - Velocidad: {vehicle.get_speed()}")
        # Mientras no se precione una tecla sigue corriendo
        if msvcrt.kbhit():
            pressedKey = msvcrt.getch()
            if pressedKey == b'1':
                #print("El vehiculo avanza")
                vehicle.up()
            elif pressedKey == b'2':
                #print("El vehiculo retrocede")
                vehicle.down()
            elif pressedKey == b'3':
                #print("El vehiculo gira a la derecha y avanza")
                vehicle.right()
            elif pressedKey == b'4':
                #print("El vehiculo gira a la izquierda y avanza")
                vehicle.left()
            elif pressedKey == b'5':
                #print("El vehiculo se detiene")
                vehicle.stop()
            elif pressedKey == b'6':
                print("Has salido de la simulacion")
                done = True
            else:
                print(f"Key Pressed: {pressedKey}")
        if done:
            break
        time.sleep(0.5)


if __name__ == "__main__":
    main()

