import pygame

# level constants
# the width and height must be also in blankLevelGenerator.py
LevelWidth = 16
LevelHeight = 9

# TODO since we use a wide screen ratio for our room size we must make it scale for other ratios somehow

class Level:
    
    """
    The Level is used to store information about the level XD
    
    for the tuples the entities that are stored in them will only appear once in the game.
    and the entites stored in list appear more than once 

    ( tile_width, tile_height )
    its the location on the grid from the origin
    the origin is the pygame's origin eg top left corner since we read the file this way

    the level entities are :
    b : block
    t : trap
    p : player spawnpoint
    T : twin spawnpoint
    e : exit spawnpoint

    """

    def __init__(self, LevelStruct:list = None ) -> None:

        if LevelStruct != None:
            self.blocks:list = LevelStruct["blocks"]
            self.traps:list = LevelStruct["traps"]
            self.player:tuple = LevelStruct["spawnPoint"]
            self.twin:tuple = LevelStruct["twinSpawnPoint"]
            self.exit:tuple = LevelStruct["exit"]
        else:
            self.blocks:list = []
            self.traps:list = []
            self.player:tuple = ()
            self.twin:tuple = ()
            self.exit:tuple = ()

    def addBlock( self, row:int, column:int ) -> None:
        self.blocks.append( ( row, column ) )
    
    def addTraps( self, row:int, column:int ) -> None:
        self.traps.append( ( row, column ) )
    
    def SetPlayerSpawnPoint( self, row:int, column:int ) -> None:
        self.player = ( row, column )
    
    def SetTwinSpawnPoint( self, row:int, column:int ) -> None:
        self.twin = ( row, column )
    
    def SetExitSpawnPoint( self, row:int, column:int ) -> None:
        self.exit = ( row, column )
    
    def GetAsDict( self ) -> dict:
        LevelStruct = {}

        LevelStruct["blocks"] = self.blocks
        LevelStruct["traps"] = self.traps
        LevelStruct["spawnPoint"] = self.player
        LevelStruct["twinSpawnPoint"] = self.twin
        LevelStruct["exit"] = self.exit

        return LevelStruct
    
    def Getblocks( self ) -> list:
        return self.blocks

        

        

def LoadLevel( levelName:str ) -> Level:
    with open(f"levels/{levelName}", "r") as file:
        data = file.read().split("\n")
    level = Level()
    for row in range( LevelHeight ):
        for column in range( LevelWidth ):
            match data[row][column]:
                case "b":
                    level.addBlock( row, column )
                case "t":
                    level.addTraps( row, column )
                case "p":
                    level.SetPlayerSpawnPoint( row, column )
                case "T":
                    level.SetTwinSpawnPoint( row, column )
                case "e":
                    level.SetExitSpawnPoint( row, column ) 

    return level

def loadLevelByName( Name:str ) -> Level:
    return LoadLevel( Name )

def loadLevelById( Id:int ) -> Level:
    return LoadLevel( f"level{Id}" )


if __name__ == '__main__':
    # this is for testing
    print( loadLevelById( 0 ).GetAsDict() )