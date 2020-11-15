import time
import queue
import threading
import concurrent.futures

from .servo import Servomotor
from .parachoque import Parachoque


class Vehicle:
    def __init__(self):
        self._position_y = 20
        self._position_x = 20
        # Estados: [0]: Stop [1]:Up [2]: Down [3]:right [4]:left [5]: girando
        self._state = 0

        # Se instancian los modelos
        self._servo1 = Servomotor(90, "1")
        self._servo2 = Servomotor(90, "2")
        self._parachoque = Parachoque()

        # Se crean las colas que utilizaran los hilos para comunicarse
        self._servo1_queue = queue.Queue()
        self._servo2_queue = queue.Queue()
        self._parachoque_queue = queue.Queue()

    def run(self):

        # Se crean los hilos y se ejecutan
        threading.Thread(target=self._servo1.loop,
                         args=(self._servo1_queue,), daemon=True).start()
        threading.Thread(target=self._servo2.loop,
                         args=(self._servo2_queue,), daemon=True).start()
        threading.Thread(target=self._parachoque.loop, args=(
            self._parachoque_queue,), daemon=True).start()
        threading.Thread(target=self.loop,
                         args=(), daemon=True).start()

        self.stop()

    def loop(self):

        while True:
            print(
                f"Posición del vehiculo: ({self._position_x},{self._position_y})")

            if (self._position_y < 23 and self._position_y > 17 and self._position_x < 23 and self._position_x > 17):
                if self._state != 0:
                    if self._state == 1:
                        self._position_y += 1
                    if self._state == 2:
                        self._position_y -= 1
                    if self._state == 3:
                        self._position_x += 1
                    if self._state == 4:
                        self._position_x -= 1
            else:
                self._colision()

            time.sleep(10)

    def _colision(self):
        print("Se produjo una colision")
        self._parachoque_queue.put(True)
        if self._state == 1:
            self._position_y -= 1
        if self._state == 2:
            self._position_y += 1
        if self._state == 3:
            self._position_x -= 1
        if self._state == 4:
            self._position_x += 1
        self.stop()
        self._parachoque_queue.put(False)

    def get_speed_servos(self):
        return f"Servo_1: {self._servo1.speed} Servo_2: {self._servo2.speed}"

    def get_parachoque_queue(self):
        return self._parachoque_queue

    def get_parachoque_status(self):
        return self._parachoque.status

    def get_position_y(self):
        return self._position_y
    
    def get_position_x(self):
        return self._position_x

    def _forward(self):
        self._servo1_queue.put(110)
        self._servo2_queue.put(66)
        time.sleep(1)

    def _turnRight(self):
        self._servo1_queue.put(180)
        self._servo2_queue.put(85)
        time.sleep(1)

    def _turnLeft(self):
        self._servo1_queue.put(95)
        self._servo2_queue.put(0)

    def stop(self):
        self._servo1_queue.put(90)
        self._servo2_queue.put(90)
        self._state = 0

    def up(self):
        # Avanza hacia arriba
        if self._state != 1:
            if self._state == 2:
                self._turnLeft()
                self._turnLeft()
            if self._state == 3:
                self._turnLeft()
            if self._state == 4:
                self._turnRight()
            self._forward()
            self._state = 1

    def down(self):
        # Avanza hacia abajo
        if self._state != 2:
            if self._state == 1:
                self._turnLeft()
                self._turnLeft()
            if self._state == 3:
                self._turnLeft()
            if self._state == 4:
                self._turnRight()
            self._forward()
            self._state = 2

    def right(self):
        # Avanza hacia la derecha
        if self._state != 3:
            if self._state == 1:
                self._turnLeft()
            if self._state == 2:
                self._turnRight()
            if self._state == 4:
                self._turnLeft()
                self._turnLeft()
            self._forward()
            self._state = 3

    def left(self):
        # Avanza hacia la izquierda
        if self._state != 4:
            if self._state == 1:
                self._turnRight()
            if self._state == 2:
                self._turnLeft()
            if self._state == 3:
                self._turnLeft()
                self._turnLeft()
            self._forward()
            self._state = 4
