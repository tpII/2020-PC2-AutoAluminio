import math
import time
import threading

class Vehicle:
    def __init__(self):
        # Cada posición en x e y son 0.5 metros
        self._position_y = 10
        self._position_x = 10

        # Radio de la rueda en metros
        self._wheel_radius = 0.0325

        # Estados:[0]:stop [1]:Up [2]: Down [3]:right [4]:left 
        self._state = 0

        # Velocidad del vehiculo
        self._speed = 0

        # Flasg que le indican al hilo de los motores que acción realizar
        self._flagStop = True
        self._flagDown = False
        self._flagUp = False
        self._flagRight = False
        self._flagLeft = False
        
        # Elementos que componen el vehiculo
        self._motor_1 = 0
        self._motor_2 = 0
        self._parachoque = False

    def run(self):
        # Pone en ejecución el hilo del vehiculo y de los motores
        threading.Thread(target=self._loop,args=(), daemon=True).start()
        threading.Thread(target=self._motores_loop,args=(), daemon=True).start()
        # Se inicializa en estado stop
        self.stop()

    def _loop(self):
        while True:

            if (self._position_y < 20 and self._position_y > 0 and self._position_x < 20 and self._position_x > 0):
                
                if (not self._flagStop):
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
        if self._state == 1:
            self._position_y -= 1
        if self._state == 2:
            self._position_y += 1
        if self._state == 3:
            self._position_x -= 1
        if self._state == 4:
            self._position_x += 1
        self.stop()
        time.sleep(1)
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
        self._motor_1 = 145
        self._motor_2 = 145
        self._speed = round((self._motor_1 * self._wheel_radius * 2 * 3.14)/60, 2)
        self._flagStop = False
        
        
    def _turnRight(self):
        self._motor_1 = -145
        self._motor_2 = 145
        self._speed = 0
        time.sleep(1)

    def _turnLeft(self):
        self._motor_1 = 145
        self._motor_2 = -145
        self._speed = 0
        time.sleep(1)
            
    def stop(self):
        self._motor_1 = 0
        self._motor_2 = 0
        self._speed = 0
        self._state = 0
        self._flagStop = True
        

    def up(self):
        # Avanza hacia arriba
        if self._state != 1:
            self._flagUp = True

    def down(self):
        # Avanza hacia abajo
        if self._state != 2:
            self._flagDown = True

    def right(self):
        # Avanza hacia la derecha
        if self._state != 3:
            self._flagRight = True
            
    def left(self):
        # Avanza hacia la izquierda
        if self._state != 4:
            self._flagLeft = True
            
    def _motores_loop(self):
        # Se realiza la logica de control de los motores
        while True:
            if self._flagDown:
                if self._state == 1:
                    self._turnLeft()
                    self._turnLeft()
                if self._state == 3:
                    self._turnLeft()
                if self._state == 4:
                    self._turnRight()
                self._forward()
                self._state = 2
                self._flagDown = False
        
            if self._flagUp == True:
                if self._state == 2:
                    self._turnLeft()
                    self._turnLeft()
                if self._state == 3:
                    self._turnLeft()
                if self._state == 4:
                    self._turnRight()
                self._forward()
                self._state = 1
                self._flagUp = False

            if self._flagRight:
                if self._state == 1:
                    self._turnLeft()
                if self._state == 2:
                    self._turnRight()
                if self._state == 4:
                    self._turnLeft()
                    self._turnLeft()
                self._forward()
                self._state = 3
                self._flagRight = False
            
            if self._flagLeft:
                if self._state == 1:
                    self._turnRight()
                if self._state == 2:
                    self._turnLeft()
                if self._state == 3:
                    self._turnLeft()
                    self._turnLeft()
                self._forward()
                self._state = 4
                self._flagLeft = False
            time.sleep(1)
