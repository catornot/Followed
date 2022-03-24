from .block import Block

class Player(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (0, 255, 255))
        self.HasInventory = True
        self.inventory = { "keys": 0 }
