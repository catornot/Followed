from level import Level
from main import Main
from utils import *
from _thread import start_new_thread
from time import sleep
from classes.twin import Twin
from classes.exit import Exit
from classes.boundary import Boundary
from classes.trap import Trap
from classes.key import Key
from classes.player import Player
import pytest
import pygame
import os
import sys


def test_level_class():
    testLevel = Level()
    testLevel.loadLevelByName("testlevel")
    assert len( testLevel.GetTraps() ) != 0
    assert len( testLevel.GetBoundaries() ) != 0
    assert len( testLevel.GetKeys() ) != 0

def test_blocks():
    exit = Exit(0,0)
    assert exit.NeedsKey == True

    key = Key( 1,0 )
    assert IsAPickedUp( key ) == True

    player = Player(0,0)
    player.PickupBlock( key )
    assert HasInventory(player) == True
    assert HasKey( player ) == True

    twin = Twin( 1,0 )
    assert IsTwin( twin ) == True

    trap = Trap( 1,0 )
    assert IsTrap( trap ) == True

    


# def test_game():
#     os.environ["SDL_VIDEODRIVER"] = "dummy"
#     game = Main()
#     print( "test4" )
#     start_new_thread( game.loop(), () )
#     print( "test1" )
#     sleep(1)
#     print( "test2" )
#     game.shutdown()
#     print( "test3" )