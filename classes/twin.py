from .block import Block

class Twin(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (255, 0, 100))
        self.symbol = "t"

    def move_toward(self, x, y):
        dx = self.x - x
        dy = self.y - y

        direction = None
        if dx == 0 and dy == 0:
            return None
        if dy > 0 and dy >= dx:
            direction = "up"
        elif dy < 0 and dy < dx:
            direction = "down"
        elif dx > 0 and dx >= dy:
            direction = "left"
        else:
            direction = "right"
        return direction
