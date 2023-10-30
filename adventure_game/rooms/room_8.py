import adventure_game.utils as utils

from colorama import Fore, Style

room8_inventory = {
    'rope': 1
}

room8_state = {
    'ocean': True,
    'boat': True,
    'potion': False,
    'map': False
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
    You fell into the OCEAN and are confronted by a BIG OCTOPUS!
    \n\tMake a choice: Will you fight/flea the OCTOPUS or take the ROPE ladder back into the ship?
    '''

    print( Fore.LIGHTYELLOW_EX + Style.NORMAL + description + Style.RESET_ALL)

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
            if room8_state['ocean'] == False:
                print("")
            # Use your hand drawn map to help you think about what is valid
                if direction == 'west':
                    next_room = 4
                    done_with_room = True
                elif direction == 'north':
                    next_room = 6
                    done_with_room = True
                else:
                    # In this room, there is nowhere else to go.
                    print("CLIMB or FLEE!")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room8_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room8_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == "rope":
                go_back = room8_state['ocean']
                if go_back:
                    room8_state['ocean'] = False
                    print("You climb the ROPE LADDER back onto the ship!")
            if use_what == "boat":
                boat_state = room8_state['boat']
                if boat_state:
                    room8_state['boat'] = False
                    room8_state['potion'] = True
                    print("\nThe BOAT will work, but right now it's tiny!")
            if use_what == "potion":
                potion_state = room8_state['potion']
                if potion_state:
                    room8_state['potion'] = False
                    room8_state['map'] = True
                    print("\nThe POTION enlarges the BOAT, and you climb inside!...but where to next...")
            if use_what == "map":
                map_state = room8_state['map']
                if map_state:
                    room8_state['map'] = False
                    print("\n\tYOU WIN!"
                          "\n\tWith the handy MAP you have found a way to escape the treacherous SHIP and sail toward dry land!"
                          "\n\tSuddenly, however, your boat hits a rock and EVERYTHING GOES BLACK!"
                          "\n\tYou wake up 24 hours later in your bed, with no recollection of where you have been the last day"
                          "\n\tA salty breeze blows through the air...")
                    break
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room8_inventory)
        else:
            print("Command not implemented in ROOM 8,", the_command)

    # end of main while loop
    return next_room
