import adventure_game.utils as utils

from colorama import Fore, Style

room3_inventory = {
    "mango": 1,
    "meat": 1,
    "food": 1
}

room3_state = {
    'blocked': True
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
    You enter a room stored with food. 
    \n\tA large package of FOOD blocks new doorways to the SOUTH and to the EAST. 
    \n\tThe room begins to sway...
    '''

    print( Fore.CYAN + Style.NORMAL + description + Style.RESET_ALL)

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
            if room3_state['blocked'] == False:
                print("")
            # Use your hand drawn map to help you think about what is valid
                if direction == 'west':
                    next_room = 1
                    done_with_room = True
                elif direction == 'south':
                    next_room = 4
                    done_with_room = True
                elif direction == 'east':
                    next_room = 6
                    done_with_room = True
                else:
                    # In this room, there is nowhere else to go.
                    print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room3_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room3_inventory, drop_what)
            if drop_what == 'food':
                room3_state['blocked'] = False
                print("Good! Now the doorways are available. Below the package you see a MANGO and a MEAT slab...")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room3_inventory)
        else:
            print("Command not implemented in ROOM 3,", the_command)

    # end of main while loop
    return next_room
