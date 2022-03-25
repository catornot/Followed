from .block import Block

class Trap(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (255, 0, 0))
        self.symbol = "T"