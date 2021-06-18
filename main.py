# Import random so intruder's movement is randomly decided
import random

# Introduce the player to the game
print('You come home late one night; the moon lights the snowy ground. You notice an odd car across the street when '
      'you’re unlocking your door. You go through your door and lock it.\nYou take off your shoes and walk out of the '
      'mudroom. Then you go through your living room and to the kitchen to get something to eat. You hear your '
      'door’s handle rattle.\nYou go to look outside your front door, but no one is there, and you notice the car is '
      'gone, but you never heard it start.\nYou hear the window crash in the bathroom, you try to unlock your door and '
      'run, only to find that the lock is jammed. You try the windows, but their frozen shut in the winter cold.\nFind '
      'a way to trap the intruder and so you can call the cops.\n')
print('Welcome to Intruder Escapee\n')
# Tell the player the commands
print(
    'To move use \'go\' or \'move\' + a cardinal direction\nTo pick up an item use \'get\' or \'pick up\' + the item\'s name\nYou can also '
    'quit using \'quit\' or \'exit\'\n')

# Boolean for checking if the intruder has been beat or not
intruder_awake = True

# Boolean that checks if the player has gotten the bucket once because of water bucket item
had_bucket = False

# Boolean for user to enter god mode
god_mode_enabled = False

# Finished inventory
finished_inv = ['Phone', 'Duct Tape', 'String', 'Water Bucket', 'Hammer']

# Total items collected checker
total_collected_items = 0

# Initialize the player and intruder locations using starting locations, as well as the player's inventory and commands
inventory = []
player_loc = 'Mudroom'
intruder_loc = 'Bathroom'
command = ''

# These are to make sure the player and intruder don't go through the same doorway and not end the game
player_last_loc = ''
intruder_last_loc = ''

# Dictionary of rooms and their possible directions with the directions corresponding room
rooms = {'Mudroom': {'North': 'Living Room'},
         'Living Room': {'North': 'Kitchen',
                         'South': 'Mudroom',
                         'West': 'Guest Bedroom',
                         'East': 'Bedroom'},
         'Guest Bedroom': {'East': 'Living Room'},
         'Bedroom': {'North': 'Bathroom',
                     'West': 'Living Room'},
         'Bathroom': {'South': 'Bedroom',
                      'West': 'Kitchen'},
         'Kitchen': {'South': 'Living Room',
                     'West': 'Pantry',
                     'East': 'Bathroom'},
         'Pantry': {'North': 'Basement',
                    'East': 'Kitchen'},
         'Basement': {'South': 'Pantry'}
         }


# Randomized intruder movement
def intruder_loc_updater():
    # Make a list of possible directions the intruder can go
    possible_directions = []
    # Int to keep the max for the random decision if/elif tree
    max_directions = len(rooms[intruder_loc])

    # Get each direction the intruder can go based on what room the intruder is currently in
    for direction in rooms[intruder_loc]:
        possible_directions.append(direction)

    # Randomly decide which way the intruder is going
    if max_directions == 1:
        return rooms[intruder_loc][possible_directions[0]]
    else:
        return rooms[intruder_loc][possible_directions[random.randint(0, max_directions - 1)]]


# Function for the if tree of picking up items
# This checks what the player is trying to get, makes sure they're in the right room for it
# and makes sure they don't already have the item
def item_is_there(acquiring_item, loc):
    # Alerts the player that they need the bucket to get the water when they don't have a bucket
    if acquiring_item == 'Water' and acquiring_item.lower() in command and 'Bucket' not in inventory and player_loc == 'Kitchen':
        print('You\'ll need a bucket for that')
    return acquiring_item.lower() in command and player_loc == loc and acquiring_item not in inventory


loop_condition = 0

# This makes the game run until the intruder is "unconscious"
while loop_condition == 0:
    # Allow user to restart game
    if command == 'restart':
        inventory = []
        player_loc = 'Mudroom'
        intruder_loc = 'Bathroom'
        player_last_loc = ''
        intruder_last_loc = ''

    # Make sure player didn't enter the same room the killer is in and restart them
    if player_loc == intruder_loc or (player_loc == intruder_last_loc and intruder_loc == player_last_loc):
        print('The intruder found you!\n')
        print('Restarting...\n')
        inventory = []
        player_loc = 'Mudroom'
        intruder_loc = 'Bathroom'
        player_last_loc = ''
        intruder_last_loc = ''
        pass

    # Check if intruder is trapped i.e. player has all items
    if len(inventory) == 5:
        # Match items with nested for loop
        for i in inventory:
            for item in finished_inv:
                # If items match, add to total_collected_items then go to the first loop
                if i == item:
                    total_collected_items += 1
                    break
        # Make sure the player has all appropriate items, if so, player wins
        if total_collected_items == 5:
            print('You got the intruder and called the cops! The intruder was arrested and you\'re safe!\n')
            intruder_awake = False

    # Print until the player has all items
    if total_collected_items != 5:
        # Reset total_collected_items so it doesn't over-count
        total_collected_items = 0

        # Tell the player where they are
        print('You\'re currently in the', player_loc)

        # Item hints
        if player_loc == 'Mudroom':
            print('Doesn\'t look like there\'s anything useful in here...')
        elif player_loc == 'Living Room' and 'Duct Tape' not in inventory:
            print('Oh, one of my rolls of duct tape, when\'s duct tape not useful?')
        elif player_loc == 'Guest Bedroom' and 'String' not in inventory:
            print('There\'s some string on the nightstand from sewing earlier')
        elif player_loc == 'Bedroom' and 'Phone' not in inventory:
            print('My phone, should call the cops once the intruder isn\'t chasing you')
        elif player_loc == 'Pantry' and 'Bucket' not in inventory and not had_bucket:
            print('Hmm, that bucket could hold something if I make it heavy')
        elif player_loc == 'Kitchen' and 'Water Bucket' not in inventory:
            print('The water from the faucet could be useful, maybe I could make something heavy?')
        elif player_loc == 'Basement' and 'Hammer' not in inventory:
            print('A hammer, now that could do some damage!')
        elif player_loc == 'Bathroom':
            print('Nothing but healing supplies in here...')

        # Tell the player their inventory
        print('Inventory: ', end='')
        # Print commas appropriately instead of just printing a list
        last_item = 0
        for collected in inventory:
            if inventory.index(collected) != last_item:
                print(',', collected, end='')
                last_item += 1
            else:
                print(collected, end='')
        print('\n---------------------------------')

    # Get player's command
    command = input()
    print()

    # Enable god mode
    if command == 'enable god mode':
        god_mode_enabled = True
        pass

    # User command quit loop breaker
    if command == 'quit' or command == 'exit':
        break

    # Commands for 'god mode'
    if command == 'intruder location' and god_mode_enabled:
        print(intruder_loc)
    elif command == 'all items' and god_mode_enabled:
        inventory = finished_inv

    # Movement controls and intruder randomized movement
    # See intruder_loc_updater above at line 92
    # intruder_loc_updater is in each so that the killer doesn't move when the player doesn't
    if ('go' in command and 'god' not in command) or 'move' in command:
        player_last_loc = player_loc
        intruder_last_loc = intruder_loc
        if 'north' in command and 'North' in rooms[player_loc]:
            player_loc = rooms[player_loc]['North']
            intruder_loc = intruder_loc_updater()
        elif 'south' in command and 'South' in rooms[player_loc]:
            player_loc = rooms[player_loc]['South']
            intruder_loc = intruder_loc_updater()
        elif 'east' in command and 'East' in rooms[player_loc]:
            player_loc = rooms[player_loc]['East']
            intruder_loc = intruder_loc_updater()
        elif 'west' in command and 'West' in rooms[player_loc]:
            player_loc = rooms[player_loc]['West']
            intruder_loc = intruder_loc_updater()
        else:
            print('Where are you going? There\'s a wall there...')

    # Item acquirement controls
    # See item_acquirement at line 147
    if 'get' in command or 'pick up' in command:
        if item_is_there('Duct Tape', 'Living Room'):
            inventory.append('Duct Tape')
        elif item_is_there('String', 'Guest Bedroom'):
            inventory.append('String')
        elif item_is_there('Phone', 'Bedroom'):
            inventory.append('Phone')
        elif item_is_there('Bucket', 'Pantry'):
            inventory.append('Bucket')
        elif item_is_there('Water', 'Kitchen') and 'Bucket' in inventory and not had_bucket:
            inventory.remove('Bucket')
            inventory.append('Water Bucket')
            # This is so that the player can't pick up a second bucket after filling the first with water
            had_bucket = True
        elif item_is_there('Hammer', 'Basement'):
            inventory.append('Hammer')
        elif 'water' not in command or player_loc != 'Kitchen':
            # Had to add condition for custom 'can't pick up' print for water in item_acquirement function
            print('That\'s not something you can pick up...')
