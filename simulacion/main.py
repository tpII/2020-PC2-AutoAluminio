import logging
import threading
import time
import concurrent.futures
import queue
import msvcrt

from modelos.servo import Servomotor
from modelos.parachoque import Parachoque
from modelos.wall import Wall
from vehicle import vehicle_forward, vehicle_reverse, vehicle_turnRight, vehicle_turnLeft


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # Se crean las colas que utilizaran los hilos para comunicarse
    servo1_queue = queue.Queue()
    servo2_queue = queue.Queue()
    wall_queue = queue.Queue()

    # Se instancian los modelos
    servo1 = Servomotor(90, "1")
    servo2 = Servomotor(90, "2")
    parachoque = Parachoque()
    wall = Wall()

    # speed = int(
    #    input("Ingrese la velocidad del servomotor: "))
    # servo1_queue.put(speed)
    # servo2_queue.put(speed)

    # Se establece la velocidad de los servos
    vehicle_forward(servo1_queue, servo2_queue)

    # Se crean los hilos y se ejecutan
    threading.Thread(target=servo1.loop,
                     args=(servo1_queue,), daemon=True).start()
    threading.Thread(target=servo2.loop,
                     args=(servo2_queue,), daemon=True).start()
    threading.Thread(target=parachoque.loop, args=(
        wall_queue,), daemon=True).start()
    threading.Thread(target=wall.loop, args=(wall_queue,), daemon=True).start()

    # Se ejecuta el hilo principal
    done = False
    while True:

        # Mientras no se precione una tecla sigue corriendo
        if msvcrt.kbhit():
            msvcrt.getch()
            print(f" Has precionado 1 para salir")
            done = True

        # Si existe una colision: hace reversa, gira a la derecha y avanza
        if(parachoque.status == True):
            print("Se HA COLISIONADO!!!")
            time.sleep(1)
            vehicle_reverse(servo1_queue, servo2_queue)
            time.sleep(2)
            vehicle_turnRight(servo1_queue, servo2_queue)

        if done:
            break


if __name__ == "__main__":
    main()
