# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'help']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:
            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() in no_arguments:
                        result = words
                        ask_again = False;
                    else:
                        print('\tThe command: "', words[0], '" requires an argument.\n')
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result

# END ask_command


#has_a - it will take a dictionary parameter and an item name

def has_a(player_inventory, item):
    if item in player_inventory.keys():
        count = player_inventory[item]
        if count > 0:
            return True
        else:
            return False
    else:
        return False


#drop_item - it will take three parameters, player inventory and room inventory and a third parameter item name

def drop_item(player_inventory, room_inventory, item):
    if has_a(player_inventory, item):
        current_count = player_inventory[item]
        player_inventory[item] = current_count - 1
        if has_a(room_inventory, item):
            room_count = room_inventory[item]
            room_inventory[item] = room_count + 1
        else:
            room_inventory[item] = 1
        print("You dropped the", item)
    else:
        print("You cannot drop what you do not have.")


#take_item - it will take  three parameters, player inventory  and room inventory and a third parameter item name

def take_item(player_inventory, room_inventory, item):
    if has_a(room_inventory, item):
        room_count = room_inventory[item]
        room_inventory[item] = room_count - 1
        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count + 1
        else:
            player_inventory[item] = 1
    else:
        print("There is nothing to take.")

# # # # # # # # # # # # # # # # # # #  #
#
# room_status: displays the number of things in a room
#
def room_status(room_inventory):
    print("In this room you see:")

    empty = True

    for key in room_inventory.keys():
        if room_inventory[key] > 0:
            print("\t\ta", key)
            empty = False

    if empty == True:
        print("\t\t. . . sadly it is empty!")
# end room_status


# # # # # # # # # # # # # # # # # # #  #
#
# Player Status: Displays the current player inventory
#
def player_status(player_inventory):
    print("\tYou are in possession of:")
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            print("\t\t",key, ' : ', player_inventory[key])

# end player_status


def scrub_response( dirty_response ):
    result = []
    result.append(dirty_response[0])
    if len(dirty_response) > 1:
        argument = dirty_response[1]
        if argument == 'short':
            result.append("short sword")
        elif argument == "ice":
            result.append("ice pick")
        elif argument == "silver":
            result.append("silver key")
        elif argument == "wood":
            result.append("wood key")
        elif argument == "magic":
            result.append("magic key")
        else:
            result.append(argument)

    return result















