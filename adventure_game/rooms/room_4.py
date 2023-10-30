import adventure_game.utils as utils

from colorama import Fore, Style

room4_inventory = {

}

room4_state = {
    'door_locked': True,
    'other_door_locked': True,
    'dark': True
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
    You enter a pitch black room. You can see nothing, but something smells fishy...
    '''

    print( Fore.YELLOW + Style.NORMAL + description + Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]


        if the_command == 'go':
            direction = response[1]
            if room4_state['dark'] == False:
                print("")

            # Use your hand drawn map to help you think about what is valid
                if direction == 'west':
                    next_room = 2
                    done_with_room = True
                elif direction == 'north':
                    other_is_locked = room4_state['other_door_locked']
                    if not other_is_locked:
                        next_room = 3
                        done_with_room = True
                    else:
                        print("The door is locked.")
                elif direction == 'south':
                    is_locked = room4_state['door_locked']
                    if not is_locked:
                        next_room = 7
                        done_with_room = True
                    else:
                        print("The door is locked.")
                elif direction == 'east':
                    next_room = 8
                    done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("You cannot see where to go!")
        elif the_command == 'take':
            print("Currently there is nothing to take in this room.")
        elif the_command == 'drop':
            print("Currently dropping in ROOM 4 makes no sense.")
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'silver key':
                door_locked = room4_state["door_locked"]
                if door_locked:
                    room4_state['door_locked'] = False
                    print("The door to the SOUTH is unlocked!")
                else:
                    print("The door was already unlocked!")
            if use_what == 'key':
                other_door_locked = room4_state["other_door_locked"]
                if other_door_locked:
                    room4_state['other_door_locked'] = False
                    print("The door to the NORTH is unlocked!")
                else:
                    print("The door was already unlocked!")
            if use_what == 'torch':
                room_dark = room4_state["dark"]
                if room_dark:
                    room4_state['dark'] = False
                    print("Now you can see doorways to the WEST, NORTH, SOUTH, and EAST."
                          "\n The doorway to the EAST has a breeze blowing under the door...")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room4_inventory)
        else:
            print("Command not implemented in ROOM 4,", the_command)

    # end of main while loop
    return next_room
