import adventure_game.utils as utils

from colorama import Fore, Style

room10_inventory = {

}

room10_state = {
    'door_locked': True,
    'water_room': True
}


def run_room(player_inventory):
    description = '''
    . . . 
    You enter a room that suddenly begins to fill with water.
    \n\tThe water level is rising rapidly
    \n\tYou must act quickly in order to SURVIVE!...
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
            if room10_state['water_room'] == False:
                print("Dry times!")


            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 5
                done_with_room = True
            elif direction == 'east':
                is_locked = room10_state['door_locked']
                if not is_locked:
                    next_room = 12
                    done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("You must do something about the rising water level first!")
        elif the_command == 'take':
            print("Currently there is nothing to take in this room.")
        elif the_command == 'drop':
            print("Currently dropping in ROOM 10 makes no sense.")
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'magic key':
                door_locked = room10_state['door_locked']
                if door_locked:
                    room10_state['door_locked'] = False
                    print("The door to the EAST is unlocked!")
                else:
                    print("The door was already unlocked!")
            if use_what == 'cutlass':
                print("You aimlessly swing at the water, as it continues to rise...")
            if use_what == 'pistol':
                room_wet = room10_state['water_room']
                if room_wet:
                    room10_state['water_room'] = False
                    print("You aimlessly shoot your pistol at the water...but wait!"
                          "\nThe bullet pierces a hole in the wall and the water pours out into the OCEAN BELOW!"
                          "A new door appears to the EAST.")
            if use_what == 'grenade':
                print("BOOM!!!")
                return next_room-1
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room10_inventory)
        else:
            print("Command not implemented in ROOM 10,", the_command)

    # end of main while loop
    return next_room




