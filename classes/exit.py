from .block import Block

class Exit(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (255, 255, 255))
        self.NeedsKey = True
    
    def DisableKeyNeed( self ):
        self.NeedsKey = False
