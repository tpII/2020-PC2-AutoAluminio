import time

# Establece las velocidades de los servos para avanzar


def vehicle_forward(servo1_queue, servo2_queue):
    servo1_queue.put(110)
    servo2_queue.put(66)

# Establece las velocidades de los servos para retroceder


def vehicle_reverse(servo1_queue, servo2_queue):
    servo1_queue.put(66)
    servo2_queue.put(110)

# Establece las velocidades de los servos para girar a la derecha


def vehicle_turnRight(servo1_queue, servo2_queue):
    servo1_queue.put(180)
    servo2_queue.put(85)
    time.sleep(1)
    vehicle_forward(servo1_queue, servo2_queue)

# Establece las velocidades de los servos para girar a la izquierda


def vehicle_turnLeft(servo1_queue, servo2_queue):
    servo1_queue.put(95)
    servo2_queue.put(0)
    time.sleep(1)
    vehicle_forward(servo1_queue, servo2_queue)
