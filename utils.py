from classes.twin import Twin
from classes.exit import Exit
from classes.boundary import Boundary
from classes.trap import Trap
from classes.key import Key
from classes.player import Player
# from classes.block import Block

def IsKey( entity ):
    return isinstance( entity, Key )

def IsTrap( entity ):
    return isinstance( entity, Trap )

def IsPlayer( entity ):
    return isinstance( entity, Player )

def IsExit( entity ):
    return isinstance( entity, Exit )

def IsTwin( entity ):
    return isinstance( entity, Twin )

def IsBoundary( entity ):
    return isinstance( entity, Boundary )

def IsAPickedUp( entity ):
    return entity.IsPickupable

def HasInventory( entity ):
    return entity.HasInventory

def HasKey( entity ):
    if not HasInventory( entity ):
        return False
    elif entity.inventory["keys"] > 0:
        return True
    return False

def IsKeyActivated( entity ):
    if IsExit( entity ):
        if entity.NeedsKey:
            return True
    return False
    