from concurrent.futures import wait
from level import Level
from main import Main
from _thread import start_new_thread
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

# def test_game():
#     os.environ["SDL_VIDEODRIVER"] = "dummy"
#     game = Main()
#     print( "test4" )
#     start_new_thread( game.loop(), () )
#     print( "test1" )
#     wait(1)
#     print( "test2" )
#     game.shutdown()
#     print( "test3" )