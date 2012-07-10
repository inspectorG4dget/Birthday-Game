'''
Created on Sep 24, 2011

@author: ashwin

 Licensed to Ashwin Panchapakesan under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 Ashwin licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
'''
from sys import exit
from time import sleep

HELP = set(['help', 'h'])
QUIT = set(['q', 'quit'])
LIGHTS = set(['light', 'lights'])
STAIRS = set(['downstairs', 'down', 'stair', 'stairs', 'staircase'])
KITCHEN = set(['kitchen'])
TABLE = set(['table', 'dining table'])
BLOW = set(['blow', 'blow candles', 'blow candle', 'candle', 'candles'])
CUT = set(['cut', 'slice', 'cut cake', 'slice cake'])
DOOR = set(['open door', 'door', 'front door'])


def wakeup():
	print "You wake up in the morning. Everything is dark so you can't see. Turn on the lights"
	
def light():
	bulb = 	r"""
    _____
   |__ __|
     |=|
     / \
--- (   ) ---
   , `-'.
  /   |  \
 '    |   `
			"""
	
	print bulb
	print "Alright, the lights are on. Go downstairs"
	
def goDownstairs():
	stairs = """
 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,
 8                           8"b,    "Ya
 8                           8  "b,    "Ya
 8                    aaaaaaa8,   "b,    "Ya
 8                    8"b,    "Ya   "8""""""8
 8                    8  "b,    "Ya  8      8
 8             aaaaaaa8,   "b,    "Ya8      8
 8   A         8"b,    "Ya   "8"""""""      8
 8             8  "b,    "Ya  8             8
 8      aaaaaa88,   "b,    "Ya8         B   8
 8      8"b,    "Ya   "8"""""""             8
 8      8  "b,    "Ya  8                    8
 8aaaaaa8,   "b,    "Ya8                    8
 8"b,    "Ya   "8"""""""                    8
 8  "b,    "Ya  8                           8
 8,   "b,    "Ya8                           8
  "Ya   "8"""""""                           8
    "Ya  8                                  8
			"""
	print stairs
	print "You are downstairs. There's a knock on the door. You should find out who it is"
	
def openDoor():
	flower = """
                            o
                            M   o    oM""'""'""ooo
                           M   M   MM"         M
                          M"   M   MM  o""'""M   M
                         M" M   MM  Mo	M   M
                      oM""     "M  MM    ""  M   M
                  ooM""       "M   ""Moooo"	M
                 M""              "Moooooo   oMM"
                 M                     ""'""'"
                 M
                 M                         oooooooo
                 Moo                   oM""'""
                 oMMo              MM""
                oM  ""Mo        oooM""
               oM      ""'""'""'
              M"
            MM"
          oM""
         o"
     ooo""
    ""
		"""
		
	print flower
	print "Oh! someone gave you a flower for your birthday. Go to the kitchen and put the flower in a vase."
	
def kitchen():
	kitchen = """
   ____________________________________________________________________    
 /|    |__I__I__I__I__I__I__I__I__I_|       _-       %       %         |\\
  | _- |_I__I__I__I__I__I__I__I__I__|-_              %       %     _-  | 
  |    |__I__I__I__I__I__I__I__I__I_|                %       %         |
  |  - |_I__I__I__I__I__I__I__I__I__|               ,j,      %w ,      |
  | -  |__I__I__I__I__I__I__I__I__I_|  -_ -        / ) \    /%mMmMm.   |
  |    |_I__I__I__I__I__I__I__I__I__|             //|  |   ;  `.,,'    |
  |-_- /                            \             w |  |   `.,;`       |
  |   /                              \    -_       / ( |    ||         |
  |  /                                \           //\_'/    (.\    -_  |
  | /__________________________________\          w  \/   -  ``'       |
  | |__________________________________|                               |
  |    |   _______________________   |     _-            -             |
  |_-  |  |                       |  |                        _-       |
  |    |  |                     _ |  |  T  T  T  T  T                  |
  | _-_|  |    __.'`'`'`''`;__ /  |  |  |  |  |  |  |        _-     -  |
  |    |  | _/U  `'.'.,.,".'  U   |  |  | (_) |  |  |                  |
  |    |  |   |               |   |  | / \    @ [_]d b    _@_     |    |   
  |    |  |   |      `', `,   |   |  | |_|   ____         [ ]     |    |
  |_-  |  |   |   `') ( )'    |   |  | ______\__/_________[_]__   |    | 
  |    |  |   |____(,`)(,(____|   |  |/________________________\  |    |
  |    |  |  /|   `@@(@@)@)'  |\  |  | ||            _____   ||   |    |
  |    |  | //!\  @@)@@)@@@( /!\\ |  | ||   _--      \   /   ||  /|\   |
  |__lc|__|/_____________________\|__|_||____________/###\___||_|||||__|
 / -_  _ -      _ -   _-_    -  _ - _ -|| -_    _  - \___/_- || |||||-_ \ 
			"""
	
	print kitchen
	print "You're in the kitchen. Oh! What's that on the dining table? Go to the dining table"
	
def table():
	table = """
                         , 
                        (_) 
                        |-|
                        | |
                        | |
                       .| |. 
                      |'---'|
                      |~  ~~|
                  .-@'|  ~  |'@-.
                 (@ '--------'  @)
                 |'-@..__@__..@-'|
              () |~  ~ ~ ~   ~   | ()
             .||'| ~() ~   ~ ()~ |'||.
            ( || @'-||.__~__.||-'@ || )
            |'-.._  ||   @   ||  _..-'|
            |~ ~  '''---------'''  ~  |
            |  ~  ~  H A P P Y ~  ~  ~|
          [ | ~   B I R T H D A Y ~ ~ |____
         [  |         R A J I         |    ]
        [    '-..    P A T T I    ..-'    ]
       [          '''---------'''        ]
      [_________________________________]
         \ \  / /              \ \  / /
          \ \/ /                \ \/ /
          _\/ /__________________\ \/_
         [_/o/___________________\o\_]
          / /\ \                 / /\ \\
         lc/  \\_\\               /_/  \\_\\
			"""
			
	print table
	print "Oh! it a birthday cake for you. Make a wish and blow out the candles."
	
def cake():
	knife = """
   emmmmmm~~~~~~~~~~~~~~~~~~~~~~~~~\\
    ''''''|_____                    )
                '''''''''--------'''
			"""
	print "You've blown out all the candles. Time to cut the cake. Here's a knife:"
	print knife

def eat():
	slice = """
()()()()()()
|\         |
|.\. . . . |
\'.\       |
 \.:\ . . .|
  \'o\     |
   \.'\. . |
    \".\   |
     \'`\ .|
      \.'\ |
       \__\|
			"""
	smiley = """
          .............
       ....           ....
     ..	                 ..
   ..                     ..
  .    ___        ___       .
 .    / , \      / , \       .
 .    \___/      \___/        .
..                            .
..                           .
..           O              .
 .  |                    |  .
 .   \                  /  .
  .  \                 /  .
   .. \______________/  ..
     ..	\_____\  \  \/  ..
       ....   |  \  |....
       ...... |  |  |
               \___/
			"""
	print "Yay! you cut the cake. Have a piece... and give me some, too"
	print slice
	print smiley
	
def help():
	print "These are the commands available to you:\n\t",
	print '\n\t'.join((' / '.join(cat)) for cat in [HELP, QUIT, LIGHTS, STAIRS, KITCHEN, TABLE, BLOW, CUT, DOOR])

def getCommand(acceptable):
	command = raw_input("++> ").strip().lower()
	
	while command not in acceptable:
		if command in HELP:
			help()
		elif command in QUIT:
			exit(0)
		else:
			print "That is not a valid command. Try again... or type 'h' for a list of available commands"
		command = raw_input("++> ").strip().lower()
			
	return 1

if __name__ == "__main__":
	wakeup()
	
	getCommand(LIGHTS)
	light()

	getCommand(STAIRS)
	goDownstairs()
	
	getCommand(DOOR)
	openDoor()
	
	getCommand(KITCHEN)
	kitchen()
	
	getCommand(TABLE)
	table()
	
	getCommand(BLOW)
	cake()
	
	getCommand(CUT)
	eat()

	sleep(3)
	
	print """

_________00000000000___________000000000000________
______00000000_____00000___000000_____0000000______
____0000000_____________000______________00000_____
___0000000_______________0_________________0000____
__000000____________________________________0000___
__00000________________HAPPY________________ 0000__
_00000_______________BIRTHDAY_______________00000__
_00000_____________________________________000000__
__000000_______________PATTI_____________0000000___
___0000000______________________________0000000____
_____000000____________________________000000______
_______000000________________________000000________
__________00000_____________________0000___________
_____________0000_________________0000_____________
_______________0000_____________000________________
_________________000_________000___________________
_________________ __000_____00_____________________
______________________00__00_______________________
			"""

raw_input("press any key to exit")
exit(0)
