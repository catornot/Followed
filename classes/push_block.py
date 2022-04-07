from .block import Block

class PushBlock(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (50, 50, 50))
        self.symbol = "m"
    
    def moveSelf( self, origin:tuple, blockList:list ) -> bool:
        
        # TODO : test this
        # NOTE : if you use the direction and .move() function it may be easiser :)
        CanMove = True
        pos = self.get_pos()
        destination = ( pos[0] - origin[0], pos[1] - origin[1] )
        for block in self.blocks:
            if block.collide(destination[0], destination[1]):
                CanMove = False
                break
        
        return CanMove
