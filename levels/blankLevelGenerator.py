import os

LevelWidth = 16
LevelHeight = 9

"""
This script generates a blank level
"""


def main():
    
    max_level_id = 0

    for root, dirs, files in os.walk( os.path.join( os.getcwd(), "levels" ) ):
        for file in files:
            file = file.split( "." )
            if file[1] == "txt":
                if file[0].startswith( "level" ):
                    max_level_id += 1
    
    BlankLevel = ""

    for y in range(LevelHeight):
        BlankLevel += f'{"0" * LevelWidth }\n'
    
    with open(f"levels/level{max_level_id}", "w") as file:
        file.write( BlankLevel )
            
            



if __name__ == '__main__':
    main()