import adventure_game.utils as utils

from colorama import Fore, Style

room1_inventory = {

}

room1_state = {
    'door_locked': True
}


# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#
#  GO: From this room you can get to Room 2 (SOUTH) and Room 1 (East)
#  Take: There is nothing to take in this room
#  Use: There is nothing to use in this room
#
def run_room(player_inventory):
    description = '''
    Hint: To make the game easier, draw a map of the rooms as you explore.
    
    . . . Main Room . . .
    You open your eyes. The room you see is unfamiliar. You see an open
    doorway to the SOUTH. To the EAST you see a closed door. 

    '''
    print(Fore.BLUE + Style.NORMAL + description + Style.RESET_ALL)

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
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                is_locked = room1_state['door_locked']
                if not is_locked:
                    next_room = 3
                    done_with_room = True
                else:
                    print("The door is locked.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            print("There is nothing to take here.")
        elif the_command == 'drop':
            drop_what = response[1]
            if drop_what in player_inventory.keys():
                del player_inventory[drop_what]
                print("You no longer possess,", drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'key':
                door_locked = room1_state["door_locked"]
                if door_locked:
                    room1_state["door_locked"] = False
                    print("The door to the EAST is unlocked!")
                else:
                    print("The door was already unlocked!")
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room1_inventory)

    # end of while loop
    return next_room
