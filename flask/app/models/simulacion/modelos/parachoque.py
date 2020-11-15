import time
import queue


class Parachoque:
    def __init__(self):
        self._status = False

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def loop(self, wall_queue):
        while True:
            try:
                # Si existe colision con un muro status se estableve en True
                self._status = wall_queue.get(timeout=1)
            except queue.Empty:
                pass
            # Imprime el estado
            self.get_status()
            time.sleep(7)

    def get_status(self):
        if(self._status == True):
            print("\nEl parachoque ha colisionado")
        else:
            print("\nEl parachoque no ha colisionado")
