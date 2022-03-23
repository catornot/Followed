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
            self.boundaries:list = LevelStruct["boundaries"]
            self.traps:list = LevelStruct["traps"]
            self.player:Player = LevelStruct["player"]
            self.twin:Twin = LevelStruct["twin"]
            self.exit:Exit = LevelStruct["exit"]
            self.keys:list = LevelStruct["keys"]
        else:
            self.traps:list = []
            self.exit:Exit = Exit(0, 0)
            self.player:Player = Player(0, 0)
            self.twin:Twin = Twin(0, 0)
            self.boundaries:list = []
            self.keys:list = []
    
    def load_level( self, levelName:str ) -> None:

        self.ClearLevel()

        with open(f"levels/{levelName}.txt", "r") as file:
            data = file.read().split("\n")

        _map = []
        for row in data:
            _map.append(list(row))

        level = Level()
        for y, row in enumerate(_map):
            for x, block in enumerate(row):
                match block:
                    case "p":
                        self.SetPlayer(x, y)
                    case "t":
                        self.SetTwin(x, y)
                    case "b":
                        self.addBoundaries(x, y)
                    case "T":
                        self.addTrap(x, y)
                    case "e":
                        self.SetExit(x, y)
                    case "k":
                        self.addKey(x, y)

        return level
    
    def loadLevelByName(self, Name:str) -> None:
        self.load_level(Name)

    def loadLevelByIndex( self, Index:int ) -> None:
        self.load_level( f"level{Index}" )

    def move(self, direction):
        blocks = [self.player, self.twin, self.exit]
        blocks += [boundary for boundary in self.boundaries]
        blocks += [trap for trap in self.traps]
        blocks += [key for key in self.keys]

        player_going_to = [0, 0]

        match direction:
            case "left":
                player_going_to[0] = self.player.x - 1
                player_going_to[1] = self.player.y
            case "right":
                player_going_to[0] = self.player.x + 1
                player_going_to[1] = self.player.y
            case "up":
                player_going_to[0] = self.player.x
                player_going_to[1] = self.player.y - 1
            case "down":
                player_going_to[0] = self.player.x
                player_going_to[1] = self.player.y + 1

        for block in blocks:
            if block.collide(player_going_to[0], player_going_to[1]) and block != self.player:
                if isinstance(block, Key):
                    # What to do if you hit a key
                    continue
                elif isinstance(block, Exit):
                    # What to do if you hit a Exit
                    continue
                break
        else:
            self.player.move(direction)

        twin_direction = self.twin.move_toward(self.player.x, self.player.y)
        twin_going_to = [0, 0]

        match twin_direction:
            case "left":
                twin_going_to[0] = self.twin.x - 1
                twin_going_to[1] = self.twin.y
            case "right":
                twin_going_to[0] = self.twin.x + 1
                twin_going_to[1] = self.twin.y
            case "up":
                twin_going_to[0] = self.twin.x
                twin_going_to[1] = self.twin.y - 1
            case "down":
                twin_going_to[0] = self.twin.x
                twin_going_to[1] = self.twin.y + 1

        for block in blocks:
            if block.collide(twin_going_to[0], twin_going_to[1]) and block != self.twin:
                if isinstance(block, Key):
                    # What to do if you hit a key
                    continue
                elif isinstance(block, Exit):
                    # What to do if you hit a Exit
                    continue
                break
        else:
            self.twin.move(twin_direction)

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
    
    def addBoundaries( self, x:int, y:int ) -> None:
        self.boundaries.append(Boundary(x, y))
    
    def addTrap( self, x:int, y:int ) -> None:
        self.traps.append(Trap(x, y))
    
    def addKey( self, x:int, y:int ) -> None:
        self.keys.append(Key(x, y))
    
    def SetPlayer( self, x:int, y:int ) -> None:
        self.player.move_to(x, y)
    
    def SetTwin( self, x:int, y:int ) -> None:
        self.twin.move_to(x, y)
    
    def SetExit( self, x:int, y:int ) -> None:
        self.exit.move_to(x, y)
    
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
    
    def GetKeys( self ) -> list:
        return self.keys
    def GetKeyByIndex( self, Index:int ) -> tuple:
        return self.keys[Index]
    
    def GetPlayer( self ) -> Player:
        return self.player
    
    def GetTwin( self ) -> Twin:
        return self.twin
    
    def GetExit( self ) -> tuple:
        return self.exit