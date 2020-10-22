import time
import queue


class Servomotor:
    def __init__(self, speed, number):
        self._speed = speed
        self._number = number

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def loop(self, speed_queue):
        while True:
            try:
                # recibe de la cola del servo la velocidad a establecer
                self._speed = speed_queue.get(timeout=1)
            except queue.Empty:
                pass
            # Imprime la velocidad
            self.get_speed()
            time.sleep(5)

    def get_speed(self):
        print(
            f"\n [Servo {self._number}]La velocidad del servo es: {self._speed}")
