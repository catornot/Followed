from classes.player import Player
from classes.twin import Twin
from classes.boundary import Boundary

# level constants
# the width and height must be also in blankLevelGenerator.py
LevelWidth = 30
LevelHeight = 20

class Level(object):
    
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
            self.blocks:list = LevelStruct["boundaries"]
            self.traps:list = LevelStruct["traps"]
            self.player:Player = LevelStruct["player"]
            self.twin:Twin = LevelStruct["twin"]
            self.exit:tuple = LevelStruct["exit"]
        else:
            self.traps:list = []
            self.player:tuple = ()
            self.exit:tuple = ()
            self.player:Player = Player(0, 0)
            self.twin:Twin = Twin(0, 0)
            self.boundaries:list = []
    
    def load_level( self, levelName:str ) -> None:
        with open(f"levels/{levelName}", "r") as file:
            data = file.read().split("\n")
        level = Level()
        for row in range( LevelHeight ):
            for column in range( LevelWidth ):
                match data[row][column]:
                    case "p":
                        self.player.move_to(column, row)
                    case "t":
                        self.twin.move_to(column, row)
                    case "b":
                        self.boundaries.append(Boundary(column, row))
                    case "T":
                        self.addTraps( column, row )
                    case "e":
                        self.SetExit( column, row )

        return level
    
    def loadLevelByName( self, Name:str ) -> None:
        self.load_level( Name )

    def loadLevelByIndex( self, Index:int ) -> None:
        self.load_level( f"level{Index}" )

    def load_level(self, level):
        self.player.move_to(0, 0)
        self.twin.move_to(0, 0)
        self.boundaries.clear()

        # for y, row in enumerate(level):
        #     for x, block in enumerate(row):
        #         match block:
                    

    def move(self, direction):
        positions = [[boundary.x, boundary.y] for boundary in self.boundaries]

        match direction:
            case "left":
                if not [self.player.x - 1, self.player.y] in positions and not [self.twin.x + 1, self.twin.y] in positions:
                    self.player.move("left")
                    self.twin.move("right")
                    return True
            case "right":
                if not [self.player.x + 1, self.player.y] in positions and not [self.twin.x - 1, self.twin.y] in positions:
                    self.player.move("right")
                    self.twin.move("left")
                    return True
            case "up":
                if not [self.player.x, self.player.y - 1] in positions and not [self.twin.x, self.twin.y + 1] in positions:
                    self.player.move("up")
                    self.twin.move("down")
                    return True
            case "down":
                if not [self.player.x - 1, self.player.y + 1] in positions and not [self.twin.x, self.twin.y - 1] in positions:
                    self.player.move("down")
                    self.twin.move("up")
                    return True

        return False

    def render(self, surface) -> None:
        self.player.render(surface)
        self.twin.render(surface)

        for boundary in self.boundaries:
            boundary.render(surface)
    
    def addBoundaries( self, row:int, column:int ) -> None:
        self.blocks.append( ( row, column ) )
    
    def addTraps( self, row:int, column:int ) -> None:
        self.traps.append( ( row, column ) )
    
    def SetPlayer( self, row:int, column:int ) -> None:
        self.player.move_to(column, row)
    
    def SetTwin( self, row:int, column:int ) -> None:
        self.twin.move_to(column, row)
    
    def SetExit( self, row:int, column:int ) -> None:
        self.exit = ( row, column )
    
    def GetAsDict( self ) -> dict:
        LevelStruct = {}

        LevelStruct["boundaries"] = self.boundaries
        LevelStruct["traps"] = self.traps
        LevelStruct["player"] = self.player
        LevelStruct["twin"] = self.twin
        LevelStruct["exit"] = self.exit

        return LevelStruct
    
    def GetBoundaries( self ) -> list:
        return self.boundaries
    def GetBoundaryByIndex( self, Index:int ) -> Boundary:
        return self.boundaries[Index]
    
    def GetTraps( self ) -> list:
        return self.traps
    def GetTrapsByIndex( self, Index:int ) -> tuple:
        return self.traps[Index]
    
    def GetPlayer( self ) -> Player:
        return self.player
    
    def GetTwin( self ) -> Twin:
        return self.twin
    
    def GetExit( self ) -> tuple:
        return self.exit
