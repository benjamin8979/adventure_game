import adventure_game.utils as utils

from colorama import Fore, Style

room11_inventory = {

}

room11_state = {
    "shrimp": True
}


# # # # # # # # #
#   Room 11
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    description = '''
    . . . 
    As you enter the room, you are confronted by a beast with the body of a man and the head of a shrimp.
    \n\tIt is VERY UGLY but VERY DANGEROUS
    \n\tCombat it or PERISH!...
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
            if room11_state['shrimp'] == False:
                print("MUNCH! CRUNCH!")
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 7
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("You must get past the SHRIMP MAN before you can continue!")
        elif the_command == 'take':
            print("Currently there is nothing to take in this room.")
        elif the_command == 'drop':
            print("Currently dropping in ROOM 11 makes no sense.")
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'cutlass':
                print("THE SHRIMP MAN CANNOT BE DEFEATED BY THAT!")
            if use_what == 'pistol':
                print("THE SHRIMP MAN CANNOT BE DEFEATED BY THAT!")
            if use_what == 'grenade':
                print("THE SHRIMP MAN CANNOT BE DEFEATED BY THAT!")
            if use_what == 'mango':
                print("The SHRIMP MAN is enfuriated by you offering him fruit!")
            if use_what == 'meat':
                give_meat = room11_state['shrimp']
                if give_meat:
                    room11_state['shrimp'] = False
                    print("You have distracted the SHRIMP MAN with the meat slab!"
                          "QUICKLY proceed to another room!")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room11_inventory)
        else:
            print("Command not implemented in ROOM 11,", the_command)

    # end of main while loop
    return next_room



