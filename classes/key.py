from .block import Block

class Key(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (255, 255, 0))