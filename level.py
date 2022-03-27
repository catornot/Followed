from classes.player import Player
from classes.twin import Twin
from classes.exit import Exit
from classes.boundary import Boundary
from classes.trap import Trap
from classes.key import Key
from classes.text import Text
from classes.push_block import PushBlock

from utils import *

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
            self.text:list = LevelStruct["text"]
        else:
            self.traps:list = []
            self.exit:Exit = Exit(0, 0)
            self.player:Player = Player(0, 0)
            self.twin:Twin = Twin(0, 0)
            self.boundaries:list = []
            self.keys:list = []
            self.text:list = []
        
        self.requestNextLevel = False
        self.requestRestartLevel = False

        self.maxMoves = 10
        self._generateListOfBlocks()
    
    def load_level( self, levelName:str ) -> None:

        self.ClearLevel()

        with open(f"levels/{levelName}.txt", "r") as file:
            data = file.read().split("\n")

        map_data = data[:LevelHeight]
        script_data = data[LevelHeight+1:]

        _map = []
        for row in map_data:
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
                    case "d":
                        self.addText( x,y )
        
        for script in script_data:

            if script.startswith( "!maxMoves" ):
                self.maxMoves = int( script.split("=")[1] )

            elif script.startswith( "!ExitNeedsKey" ):
                if not bool( script.split("=")[1] ): self.exit.DisableKeyNeed()
            
            elif script.startswith( "!AddText" ):
                posNtext = script.split("=")[1].split(",")
                self.addText( int( posNtext[0] ) * 32, int( posNtext[1] ) * 32 )
                self.text[ len(self.text) - 1 ].SetText( posNtext[2] )

        return level
    
    def loadLevelByName(self, Name:str) -> None:
        self.load_level(Name)

    def loadLevelByIndex( self, Index:int ) -> None:
        self.load_level( f"level{Index}" )

    def move(self, direction):
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
        
        resetBlockList = False
        for block in self.blocks:
            if block.collide(player_going_to[0], player_going_to[1]) and block != self.player:
                if IsKey( block ):
                    self.player.PickupBlock( block )
                    resetBlockList = True
                    self.RemoveBlockByPosition( player_going_to )
                    continue
                elif IsTrap( block ):
                    self.requestRestartLevel = True
                elif IsKeyActivated( block ):
                    if IsExit( block ):
                        self.requestNextLevel = True
                    continue
                break
        else:
            self.player.move(direction)
        
        if resetBlockList:
            self._generateListOfBlocks()

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

        for block in self.blocks:
            if block.collide(twin_going_to[0], twin_going_to[1]) and block != self.twin:
                if IsKey( block ):
                    self.keys.remove(block)
                    continue
                if IsTrap( block ):
                    self.requestRestartLevel = True
                    continue
                if IsPlayer( block ):
                    self.requestRestartLevel = True
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
        
        for text in self.text:
            text.render(surface)
    
    def ClearLevel( self ) -> None:
        self.player.move_to(0, 0)
        self.twin.move_to(0, 0)
        self.exit.move_to(0, 0)
        self.boundaries.clear()
        self.traps.clear()
        self.keys.clear()
        self.text.clear()
    
    def _generateListOfBlocks( self ) -> None:
        self.blocks = [self.player, self.twin, self.exit]
        self.blocks += [boundary for boundary in self.boundaries]
        self.blocks += [trap for trap in self.traps]
        self.blocks += [key for key in self.keys]
    
    def AddToblockList( self, entity ) -> None:
        self.blocks.append( entity )
    
    def addBoundaries( self, x:int, y:int ) -> None:
        self.boundaries.append(Boundary(x, y))
        self.AddToblockList( self.boundaries[len(self.boundaries)-1] )
    
    def addTrap( self, x:int, y:int ) -> None:
        self.traps.append(Trap(x, y))
        self.AddToblockList( self.traps[len(self.traps)-1] )
    
    def addKey( self, x:int, y:int ) -> None:
        self.keys.append(Key(x, y))
        self.AddToblockList( self.keys[len(self.keys)-1] )
    
    def SetPlayer( self, x:int, y:int ) -> None:
        self.player.move_to(x, y)
    
    def SetTwin( self, x:int, y:int ) -> None:
        self.twin.move_to(x, y)
    
    def SetExit( self, x:int, y:int ) -> None:
        self.exit.move_to(x, y)
        self._generateListOfBlocks() # here I am calling the function to override the blocks list
        # because I am lazy and I would have to search trouhgt the list to find the exit entity
    
    def addText( self, x:int, y:int ) -> None:
        self.text.append( Text(x, y) )
        self.AddToblockList( self.text[len(self.text)-1] )


    def RemoveBlockByPosition( self, TargetPosition:tuple ):

        for block in self.blocks:
            if block.collide(TargetPosition[0], TargetPosition[1]):
                if IsKey( block ):
                    self._findBlockInListAndDestroyIt( block, self.keys )
                elif IsTrap( block ):
                    self._findBlockInListAndDestroyIt( block, self.traps )
                elif IsBoundary( block ):
                    self._findBlockInListAndDestroyIt( block, self.boundaries )
                elif IsTwin( block ):
                    self.SetTwin( -1,-1 )
                elif IsExit( block ):
                    self.SetExit( -7,-1 )
                elif IsPlayer( block ):
                    self.SetPlayer( -4,-1 )
    
    def _findBlockInListAndDestroyIt( self, block, WorkingList:list ):
        for block2 in WorkingList:
            if block == block2:
                WorkingList.pop( WorkingList.index( block ) )
                return
    
    def FindBlockByPosition( self, TargetPosition:tuple ):
        for block in self.blocks:
            if block.collide(TargetPosition[0], TargetPosition[1]):
                return block


    
    def GetAsDict( self ) -> dict:
        LevelStruct = {}

        LevelStruct["boundaries"] = self.boundaries
        LevelStruct["traps"] = self.traps
        LevelStruct["player"] = self.player
        LevelStruct["twin"] = self.twin
        LevelStruct["exit"] = self.exit
        LevelStruct["keys"] = self.keys
        LevelStruct["text"] = self.text

        return LevelStruct
    
    def GetAsList( self ) -> list:
        return self.blocks
    
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
    
    def GetExit( self ) -> Exit:
        return self.exit