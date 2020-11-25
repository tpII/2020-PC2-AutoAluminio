import time
import queue
import threading
import concurrent.futures

from .servo import Servomotor
from .parachoque import Parachoque

from datetime import datetime

class Vehicle:
    def __init__(self):
        self._position_y = 20
        self._position_x = 20
        # Estados: [1]:Up [2]: Down [3]:right [4]:left 
        self._state = 1
        self._stop = True
        self._speed = 0

        # Elementos que componen el vehiculo
        self._motor_1 = 90
        self._motor_2 = 90
        self._parachoque = False

    def run(self):
        threading.Thread(target=self.loop,args=(), daemon=True).start()
        self.stop()

    def loop(self):
        while True:
            
            if (self._position_y < 23 and self._position_y > 17 and self._position_x < 23 and self._position_x > 17):
                if not self._stop:
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
            time.sleep(1)
        
    def _colision(self):
        print("Se produjo una colision")
        self._parachoque = True 
        self.stop()
        time.sleep(1)
        if self._state == 1:
            self._position_y -= 1
        if self._state == 2:
            self._position_y += 1
        if self._state == 3:
            self._position_x -= 1
        if self._state == 4:
            self._position_x += 1
        self._parachoque = False

    def get_speed(self):
        return self._speed

    def get_speed_motor_1(self):
        return self._motor_1
    
    def get_speed_motor_2(self):
        return self._motor_2

    def get_parachoque_status(self):
        return self._parachoque

    def get_position_y(self):
        return self._position_y
    
    def get_position_x(self):
        return self._position_x

    def _forward(self):
        self._motor_1 = 110
        self._motor_2 = 66
        self._speed = 1
        self._stop = False
        time.sleep(1)

    def _turnRight(self):
        self._motor_1 = 180
        self._motor_2 = 85
        time.sleep(1)

    def _turnLeft(self):
        self._motor_1 = 95
        self._motor_2 = 0
        time.sleep(1)

    def stop(self):
        self._motor_1 = 90
        self._motor_2 = 90
        self._speed = 0
        self._stop = True

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
            self._state = 1
            self._forward()
            

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
            self._state = 2
            self._forward()
            

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
            self._state = 3
            self._forward()
            

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
            self._state = 4
            self._forward()
            