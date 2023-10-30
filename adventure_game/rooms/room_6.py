import adventure_game.utils as utils

from colorama import Fore, Style

room6_inventory = {
    "map": 1
}

room6_state = {
    'door_locked': True,
    'other_locked': True
}

# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    description = '''
    . . . 
    You enter a bright room with a single table. On that table you see a MAP. 
    \n\tThe map seems to be a star map meant to guide ships to land...
    \n\tYou see the doorway to the WEST and new doorways to the EAST and to the SOUTH. 
    \n\tThe doorway to the SOUTH has a breeze blowing under the door...
    '''

    print( Fore.LIGHTGREEN_EX + Style.NORMAL + description + Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'west':
                other_locked = room6_state['door_locked']
                if not other_locked:
                    next_room = 3
                    done_with_room = True
            elif direction == 'south':
                next_room = 8
                done_with_room = True
            elif direction == 'east':
                is_locked = room6_state['door_locked']
                if not is_locked:
                    next_room = 9
                    done_with_room = True
                else:
                    print("The door is locked.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room6_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item((player_inventory, room6_inventory, drop_what))
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'key':
                door_locked = room6_state["door_locked"]
                if door_locked:
                    room6_state["door_locked"] = False
                    print("The doors to the WEST and EAST are unlocked!")
                    print("This KEY is no longer of any use!")
                else:
                    print("The door was already unlocked")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room6_inventory)
        else:
            print("Command not implemented in ROOM 6,", the_command)

    # end of main while loop
    return next_room
