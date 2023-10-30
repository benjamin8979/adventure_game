# fix to run program from our directory
import sys
import os

cwd = os.getcwd()
sys.path.append(cwd + "/./../")

import time

# room imports
import adventure_game.rooms.room_1 as r1
import adventure_game.rooms.room_2 as r2
import adventure_game.rooms.room_3 as r3
import adventure_game.rooms.room_4 as r4
import adventure_game.rooms.room_5 as r5
import adventure_game.rooms.room_6 as r6
import adventure_game.rooms.room_7 as r7
import adventure_game.rooms.room_8 as r8
import adventure_game.rooms.room_9 as r9
import adventure_game.rooms.room_10 as r10
import adventure_game.rooms.room_11 as r11
import adventure_game.rooms.room_12 as r12

# required to use colorama
from colorama import init

init()

# Default the player to the first room
room_number = 1

# Player Inventory
player_inventory = {
    'torch': 1,
    'key': 0,
    'cup': 0,
    'mango': 0,
    'meat': 0,
    'food': 0,
    'cutlass': 0,
    'pistol': 0,
    'grenade': 0,
    'map': 0,
    'rope': 0,
    'silver key': 0,
    'wood key': 0,
    'magic key': 0,
    'potion': 0
}

print("Welcome to the maze game...\n")

room_choice = {1: r1, 2: r2, 3: r3, 4: r4, 5: r5, 6: r6, 7: r7, 8: r8, 9: r9, 10: r10, 11: r11, 12: r12}

should_continue = True
while should_continue:
    if 1 <= room_number <= 12:
        room_number = room_choice[room_number].run_room(player_inventory)
    else:
        break
#

print("The game has ended...")
