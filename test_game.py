import pytest
from level import Level

def test_game_functions():
    testLevel = Level()
    testLevel.loadLevelByName("testlevel")
    assert len( testLevel.GetTraps() ) != 0
    assert len( testLevel.GetBoundaries() ) != 0
    assert len( testLevel.GetKeys() ) != 0