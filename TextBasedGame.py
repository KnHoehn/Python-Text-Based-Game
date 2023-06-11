# Kayla Hoehn

def show_item(item):
    """Function that outputs determined by what item is in the room"""
    if item == 'Space Blaster':
        print('You see a Space Blaster hanging on the wall')
    elif item == 'Space Phone':
        print('You see a Space Phone laying on the table')
    elif item == 'Space Boots':
        print('You see a pair of Space Boots in the closet')
    elif item == 'Marshmallow Moonies':
        print('You see a bowl of Marshmallow Moonies sitting on the counter')
    elif item == 'Infodisk':
        print('You see an Infodisk laying on the command center')
    elif item == 'Weight':
        print('You see a Weight sitting on the workout bench')


def show_instructions():
    """Function that prints instructions for the game"""
    print('An Alien has invaded your spaceship... Collect all 6 items to defeat the Alien')
    print('Movement commands: Go North, Go South, Go East, Go West')
    print("Add to inventory: Get 'item name'")
    print("Type 'Exit' to exit game")
    print("Type 'I' to show instructions again")


def show_status(current_room, inventory):
    """Function that prints the players status"""
    print('-' * 30)
    print('You are in the', current_room['name'])
    print('Inventory: [ {} ]'.format(', '.join(inventory)))


def main():
    """The main function of the game"""

    # Dictionary that maps out the rooms and what items are contained in the rooms
    rooms = {

        'Engine Room': {'name': 'Engine Room', 'Go South': 'Control Room'},
        'Control Room': {'name': 'Control Room', 'Go North': 'Engine Room',
                         'Go West': 'Common Area', 'Item': 'Infodisk'},
        'Common Area': {'name': 'Common Area', 'Go East': 'Control Room', 'Go West': 'Kitchen',
                        'Go North': 'Armory', 'Go South': 'Gym', 'Item': 'Space Phone'},
        'Kitchen': {'name': 'Kitchen', 'Go East': 'Common Area', 'Item': 'Marshmallow Moonies'},
        'Gym': {'name': 'Gym', 'Go North': 'Common Area', 'Go East': 'Crew Quarters', 'Item': 'Weight'},
        'Crew Quarters': {'name': 'Crew Quarters', 'Go West': 'Gym', 'Item': 'Space Boots'},
        'Armory': {'name': 'Armory', 'Go South': 'Common Area',
                   'Go East': 'Entrance Vestibule', 'Item': 'Space Blaster'},
        'Entrance Vestibule': {'name': 'Entrance Vestibule', 'Go West': 'Armory'}

        }

    current_room = rooms['Engine Room']  # Sets the starting room to Engine Room

    inventory = []  # Creates and empty inventory

    # Prints the opening to the game
    print('\nAlien Text Adventure Game')
    print('-' * 30)
    print('You and your crew are on a mission on Mars when your spaceship is invaded by an Alien. You will need to')
    print('defeat the Alien before your crew becomes its’ dinner, but first you will need a collection of items')
    print('to aid you in your fight. You will need a space blaster to shoot the alien, a space phone to call')
    print('the base station for back up, space boots for gravitational manipulation to help dodge the aliens’')
    print('attacks, a bowl of Marshmallow Moonies for the energy you will need for the battle, an infodisk to learn')
    print('the aliens’ weaknesses, and a weight to buff yourself up for battle.')
    print('\nMovement commands: Go North, Go South, Go East, Go West')
    print("Add to inventory: Get 'item name'")
    print("Type 'Exit' to exit game")
    print("Type 'I' to show instructions again")

    # Creates a list of commands the user can use
    commands = ['Go North', 'Go South', 'Go East', 'Go West', 'Exit', 'I']

    while True:

        show_status(current_room, inventory)  # Prints the players status

        # Loop that accesses the show_item function to print a sentence determined by the item in the room
        if 'Item' in current_room:
            show_item(current_room['Item'])

        # Loop that determines if the player won or lost determined by the players inventory
        if current_room == rooms['Entrance Vestibule']:
            tokens = len(inventory)
            print('You see the Alien!')
            print('A battle ensues')
            print('...')
            if tokens == 6:
                print('Congratulations! You defeated the Alien!')
                print('Thank you for playing!')
                break
            else:
                print('You were eaten by the Alien! Game over')
                break

        # Gets input from the user
        command = input('Enter your command \n> ').title()

        # This part of the loop determines which room to place the player in determined by the user input
        if command in commands:
            if command in current_room:
                current_room = rooms[current_room[command]]
            elif command == 'Exit':  # This part of the loop terminates the program if the player inputs "Exit"
                print('Thank you for playing!')
                break
            elif command == 'I':  # This part of the loop prints instructions if the player inputs "I"
                show_instructions()
            else:  # This part of the loop executes if the player inputs a direction that doesn't lead anywhere
                print("Can't go that way!")

        # This part of the loop removes the item from the dictionary and places it in the players inventory
        elif command.split()[0] == 'Get':
            item = command[4:]
            if item in current_room['Item']:
                inventory.append(item)
                current_room.pop('Item')
        else:  # This part of the loop executes if the players inputs an invalid command
            print('Invalid move!')


main()  # Accesses main
