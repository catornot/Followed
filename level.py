from classes.player import Player
from classes.twin import Twin
from classes.exit import Exit
from classes.boundary import Boundary
from classes.trap import Trap
from classes.key import Key

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
    T : trap
    p : player spawnpoint
    t : twin spawnpoint
    e : exit spawnpoint
    k : key
    """

    def __init__(self, LevelStruct:list = None ) -> None:

        if LevelStruct != None:
            self.blocks:list = LevelStruct["boundaries"]
            self.traps:list = LevelStruct["traps"]
            self.player:Player = LevelStruct["player"]
            self.twin:Twin = LevelStruct["twin"]
            self.exit:Exit = LevelStruct["exit"]
            self.keys:list = LevelStruct["keys"]
        else:
            self.traps:list = []
            self.player:Player = ()
            self.exit:Exit = Exit( 0, 0 )
            self.player:Player = Player(0, 0)
            self.twin:Twin = Twin(0, 0)
            self.boundaries:list = []
            self.keys:list = []
    
    def load_level( self, levelName:str ) -> None:

        self.ClearLevel()

        with open(f"levels/{levelName}.txt", "r") as file:
            data = file.read().split("\n")
        level = Level()
        for row in range( LevelHeight ):
            for column in range( LevelWidth ):
                match data[row][column]:
                    case "p":
                        self.SetPlayer(column, row)
                    case "t":
                        self.SetTwin(column, row)
                    case "b":
                        self.addBoundaries(column, row)
                    case "T":
                        self.addTrap( column, row )
                    case "e":
                        self.SetExit( column, row )
                    case "k":
                        self.addKey( column, row )

        return level
    
    def loadLevelByName( self, Name:str ) -> None:
        self.load_level( Name )

    def loadLevelByIndex( self, Index:int ) -> None:
        self.load_level( f"level{Index}" )

    def move(self, direction):
        positions = [[boundary.x, boundary.y] for boundary in self.boundaries]

        match direction:
            case "left":
                if not [self.player.x - 1, self.player.y] in positions:
                    self.player.move("left")
            case "right":
                if not [self.player.x + 1, self.player.y] in positions:
                    self.player.move("right")
            case "up":
                if not [self.player.x, self.player.y - 1] in positions:
                    self.player.move("up")
            case "down":
                if not [self.player.x - 1, self.player.y + 1] in positions:
                    self.player.move("down")
        
        twin_direction = self.twin.move_toward(self.player.x, self.player.y)
        match twin_direction:
            case "left":
                if not [self.twin.x - 1, self.twin.y] in positions:
                    self.twin.move("left")
            case "right":
                if not [self.twin.x + 1, self.twin.y] in positions:
                    self.twin.move("right")
            case "up":
                if not [self.twin.x, self.twin.y - 1] in positions:
                    self.twin.move("up")
            case "down":
                if not [self.twin.x, self.twin.y + 1] in positions:
                    self.twin.move("down")

    def render(self, surface) -> None:
        self.player.render(surface)
        self.twin.render(surface)
        self.exit.render(surface)

        for boundary in self.boundaries:
            boundary.render(surface)
        
        for trap in self.traps:
            trap.render(surface)

        for key in self.keys:
            key.render(surface)
    
    def ClearLevel( self ) -> None:
        self.player.move_to(0, 0)
        self.twin.move_to(0, 0)
        self.exit.move_to(0, 0)
        self.boundaries.clear()
        self.traps.clear()
        self.keys.clear()
    
    def addBoundaries( self, row:int, column:int ) -> None:
        self.boundaries.append( Boundary( row, column ) )
    
    def addTrap( self, row:int, column:int ) -> None:
        self.traps.append( Trap( row, column ) )
    
    def addKey( self, row:int, column:int ) -> None:
        self.keys.append( Key( row, column ) )
    
    def SetPlayer( self, row:int, column:int ) -> None:
        self.player.move_to(column, row)
    
    def SetTwin( self, row:int, column:int ) -> None:
        self.twin.move_to(column, row)
    
    def SetExit( self, row:int, column:int ) -> None:
        self.exit.move_to( row, column )
    
    def GetAsDict( self ) -> dict:
        LevelStruct = {}

        LevelStruct["boundaries"] = self.boundaries
        LevelStruct["traps"] = self.traps
        LevelStruct["player"] = self.player
        LevelStruct["twin"] = self.twin
        LevelStruct["exit"] = self.exit
        LevelStruct["keys"] = self.keys

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