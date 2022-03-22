from .block import Block

class Boundary(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (50, 50, 50))
