from .block import Block

class Exit(Block):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, 32, 32, (255, 255, 255))
        self.symbol = "e"
        self.NeedsKey = True
    
    def DisableKeyNeed( self ) -> None:
        self.NeedsKey = False
    
    def EnableKey(self) -> None:
        self.NeedsKey = True
    
    def CanExit( self, player ) -> bool:
        if player.inventory["keys"] > 0:
            return True
        elif not self.NeedsKey:
            return True
        return False
