import time
import queue


class Wall:
    def __init__(self):
        self._wall = False

    @property
    def wall(self):
        return self._wall

    @wall.setter
    def wall(self, value):
        self._wall = value

    def loop(self, wall_queue):
        while True:
            # Cada 30 segundos existe una colision
            time.sleep(30)
            try:
                # Coloca en la cola de wall que existe una colisión
                wall_queue.put(True)
                # Cambia a que existe un muro
                self._wall = not self._wall
            except queue.Empty:
                pass
            time.sleep(1)
            # Cambia a que existe no existe un muro
            self._wall = not self._wall
            # Coloca en la cola de wall que ya no existe una colisión
            wall_queue.put(False)
