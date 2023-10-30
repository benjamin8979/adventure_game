import adventure_game.utils as utils

from colorama import Fore, Style

room9_inventory = {
    'silver key': 1,
    'wood key': 1,
    'magic key': 1
}


# # # # # # # # #
#   Room 9
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    description = '''
    . . . 
    You enter a room with three keys on a wall.
    \n\tThe keys are labeled, "Silver Key", "Wood Key", and "Magic Key".
    \n\tThere are no new doors, the only way to go is back...
    '''

    print( Fore.BLUE + Style.NORMAL + description + Style.RESET_ALL)

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
            if direction == 'west':
                next_room = 6
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room9_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.take_item(player_inventory, room9_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room9_inventory)
        else:
            print("Command not implemented in ROOM 9,", the_command)

    # end of main while loop
    return next_room
