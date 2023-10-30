import adventure_game.utils as utils

from colorama import Fore, Style


#Items currently in room

room2_inventory = {
    "key": 1,
    "cup": 1
}

room2_state = {
    'door_locked': True
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
    You enter a fowl smelling room filled with hammocks. The room begins to sway...
    \n\tYou see the open door to the NORTH and a closed door to the EAST and to the WEST. 
    \n\tThe room to the WEST has a bright light coming from it. Lying on the ground is a key and a cup.
    '''

    print( Fore.GREEN + Style.NORMAL + description + Style.RESET_ALL)

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
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 1
                done_with_room = True
            elif direction == 'east':
                next_room = 4
                done_with_room = True
            elif direction == 'west':
                is_locked = room2_state['door_locked']
                if not is_locked:
                    next_room = 5
                    done_with_room = True
                else:
                    print("The door is locked.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room2_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room2_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'key':
                print("Nope! That is not going to work.")
            if use_what == "wood key":
                door_locked = room2_state["door_locked"]
                if door_locked:
                    room2_state["door_locked"] = False
                    print("The door to the WEST is unlocked!")
                else:
                    print("The door was already unlocked!")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room2_inventory)
        else:
            print("Command not implemented in ROOM 2,", the_command)

    # end of main while loop
    return next_room






