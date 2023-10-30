import adventure_game.utils as utils

from colorama import Fore, Style

room7_inventory = {
    'boat': 1
}

room7_state = {
    'door_locked': True,
    'pirate': True
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
    You enter a room and are immediately confronted by a SKELETON PIRATE! 
    \n\tWhat will you use to combat this PIRATE...
    '''

    print( Fore.LIGHTCYAN_EX + Style.NORMAL + description + Style.RESET_ALL)

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
            if room7_state['pirate'] == False:
                print("SLICE, SMASH, CRASH!")

            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 4
                done_with_room = True
            elif direction == 'south':
                next_room = 11
                done_with_room = True
            elif direction == 'west':
                is_locked = room7_state['door_locked']
                if not is_locked:
                    next_room = 12
                    done_with_room = True
                else:
                    print("The door is locked.")
            else:
                # In this room, there is nowhere else to go.
                print("Your way is blocked by a frightful SKELETON PIRATE!")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room7_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room7_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'magic key':
                door_locked = room7_state['door_locked']
                if door_locked:
                    room7_state['door_locked'] = False
                    print("The door to the WEST is unlocked!")
                else:
                    print("The door was already unlocked!")
            if use_what == 'cutlass':
                fight_pirate = room7_state["pirate"]
                if fight_pirate:
                    room7_state['pirate'] = False
                    print("You have defeated the SKELETON PIRATE with some swift strikes of the CUTLASS!"
                          "\n You see a miniature BOAT in the skeleton pirate's hand..."
                          "\n You can now see doorways to the NORTH, SOUTH, and WEST")
            if use_what == 'pistol':
                print("The bullet from your pistol went straight through the SKELETON PIRATE'S hollow bony body, leaving him UNSCATHED!")
            if use_what == 'grenade':
                print("BOOM!!!")
                return next_room-1
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room7_inventory)
        else:
            print("Command not implemented in ROOM 7,", the_command)

    # end of main while loop
    return next_room
