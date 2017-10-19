from room import Room
from flashlight import Flashlight
from character import Enemy
from container import Container
from sniper import Sniper
from phone import Phone

heldItems = []
myHealth = 53
visitedRooms = []

# ********************************* SET UP THE ROOMS *********************************

# Kitchen
#
# Room descriptions should include interactive containers like CABINET, BIN, DESK, SHELF, SHOEBOX that contain/hide other interactive items
kitchen = Room("Kitchen","A dark and dirty room with flies buzzing around. There are dirty beakers, graduated cylinders, and pipettes in the sink. There is a CUPBOARD above the sink and a CABINET under the sink.")

# The kitchen has a CUPBOARD object that contains/hides 3 interactive items, a sponge, a plate, a can of soup
# Once this container is open, the interactive items will no longer be hidden in the container
kitchen.cupboard = Container("cupboard above the sink",["sponge","plate","can of bOPW soup"])
# The kitchen has a CABINET object that contains/hides 2 interactive items, a knife and a twinkie
# Once this container is open, the interactive items will no longer be hidden in the container
kitchen.cabinet = Container("cabinet under the sink",["knife","twinkie"])

# Create an interactive item that's show in a room (not hidden in a container) with create_room_item()
kitchen.create_room_item("spoon")
kitchen.create_room_item("rat")

#Bathroom
bathroom=Room("Bathroom","An old bathroom that had been trashed a long time ago and it looks like nobody had been in there for a long time. There is a shelf and a cabinet next to the shelf.")
bathroom.shelf = Container("shelf",["rat","empty bag of food"])
bathroom.cabinet = Container("cabinet",["Dead Spider","1 ammo"])

# Small Office
#
smalloffice = Room("Small Office","A dark room with a mess of books and papers covering the desk. There is some mail and an ozon.ru PACKAGE. You can READ a book. You can look in the DESK.")
smalloffice.desk = Container("desk",["battery","envelope"])
smalloffice.package = Container("ozon.ru package",["sheet of bubble wrap","porcelain figurine of a bear","red flashlight"])
smalloffice.create_room_item("guinea pig")
redFlashlight = Flashlight("red",0,False)

# Laboratory
#
lab = Room("Laboratory","A bright room with sunlight shining through windows secured by prison bars. There is a messy SHELF on the north wall.")
# The lab has a SHELF object that contains 3 interactive items. Shelf gets a third argument because you'd say ON the shelf, not IN the shelf
lab.shelf = Container("shelf",["brass key","spork","yellow flashlight"],"on")
lab.create_room_item("rat")
yellowFlashlight = Flashlight("yellow",1,True)
#Library
#
library=Room("Library","It's a mysterious place very dark and very quiet. You see a DESK as well as a SHELF.")
library.desk=Container("inside the desk.",["phone battery","quarter"])
library.shelf=Container("on the shelf.",["sniper","can of soup"])
library.create_room_item("rat")
library.create_room_item("fork")
# Water storage
#
waterstorage = Room("Water storage","A dark and dirty room with Spiders all around. There are dirty CANS, and jumper cables. Theres a CABINET and has important stuff on it ")
waterstorage.cabinet = Container("cabinet",["1 AMMO","warter bottle"])
waterstorage.cans = Container("In the Can",["phone","energy drink"])
waterstorage.create_room_item("can of spinach")
waterstorage.create_room_item("spork")


# Supply Closet
#
supplycloset = Room("Supply Closet","A small dark room with a musty smell. On one side is a filing CABINET and a large plastic BIN. On the other side is a SHELF with supplies and a SHOEBOX.")

# Create a fake room called locked that represents all permenently locked doors
#
locked = Room("locked","")

# Connect rooms. These are one-way connections.
kitchen.link_room(library, "EAST")
kitchen.link_room(smalloffice, "SOUTH")
kitchen.link_room(bathroom, "WEST") # Need to add a link from bathroom back to kitchen

library.link_room(kitchen, "WEST")
library.link_room(locked, "EAST")
library.link_room(locked, "NORTH")
library.link_room(locked, "SOUTH")

supplycloset.link_room(smalloffice, "EAST")
smalloffice.link_room(kitchen, "NORTH")
smalloffice.link_room(lab, "EAST")
smalloffice.link_room(waterstorage, "SOUTH")
waterstorage.link_room(smalloffice, "NORTH")
smalloffice.link_room(supplycloset, "WEST")
lab.link_room(locked, "SOUTH")
lab.link_room(smalloffice, "WEST")
current_room = kitchen

# Set up characters
dmitry = Enemy("Dmitry", "A smelly zombie")
dmitry.set_speech("Brrlgrh... rgrhl... brains...")
dmitry.set_weaknesses(["FORK","SPORK","KNIFE"])
supplycloset.set_character(dmitry)

# This is a procedure that simply prints the items the player is holding and tells them if they can do something with that item
def playerItems():
    # Print out the player's Held Items and let player know if they can USE an item to fight a character or something
    if len(heldItems) == 1:
        print("You are holding a "+heldItems[0])
        print("You can DROP "+heldItems[0].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name)
    elif len(heldItems) >= 2:
        print("Your hands are full. You must drop something before you can pick anything else up.")
        print("You are holding a "+heldItems[0]+" and a "+heldItems[1])
        print("You can DROP "+heldItems[0].upper()+" or DROP "+heldItems[1].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name+" or USE "+heldItems[1].upper())
    # ********************************* SPECIAL ITEM INTERFACES *********************************
    # If holding a special item, then display the item's interface with get_interface()
    if "red flashlight" in heldItems:
        redFlashlight.get_interface(heldItems,current_room)
    if "yellow flashlight" in heldItems:
        yellowFlashlight.get_interface(heldItems,current_room)
    if "1 ammo" in heldItems:
        1-ammo.get_interface(heldItems,current_room) # 1-ammo needs to be instanciated in the bathroom set up section above


# This fuction checks the player's command and then runs the corresponding method
def checkUserInput(current_room,command,heldItems):
    # Convert it to ALL CAPS
    command = command.upper()
    # All possible user input commands go here
    print("\n")
    
    # ********************************* SPECIAL USER INPUT *********************************
    # If holding a special item, then check for that item's UI keywords with check_input()
    if "red flashlight" in heldItems and "RED FLASHLIGHT" in command:
        redFlashlight.check_input(command,heldItems,current_room)
    elif "yellow flashlight" in heldItems and "YELLOW FLASHLIGHT" in command:
        yellowFlashlight.check_input(command,heldItems,current_room)

    # ********************************* USE, TAKE, DROP *********************************
    # Use an item to fight an enemy
    elif "USE " in command and current_room.get_character() is not None:
        # command[4:] is used to get the characters typed after "USE "
        enemyHealth = current_room.character.fight(command[4:])
        if enemyHealth < 1:
            print(current_room.character.name+" is dead")
            current_room.remove_character() # If the enemy is dead, then remove them from the room
    # Take lets you pick up an item
    elif "TAKE " in command:
        # command[5:] is used to get the characters typed after "TAKE "
        heldItems = current_room.take_room_item(command[5:],heldItems)
    # Drop lets you set down an item
    elif "DROP " in command:
        # command[5:] is used to get the characters typed after "DROP "
        heldItems = current_room.add_room_item(command[5:],heldItems)
    # Talk and Fight aren't currently used in this version of the game, but could be implemented in your version of the game
    elif "TALK" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif "FIGHT" in command and current_room.get_character() is not None:
        current_room.character.talk()
    
    # ********************************* ROOM SPECIFIC USER INPUTS *********************************
    # Interactive containers look like this...   elif current_room.name == "Laboratory" and command == "SHELF"
    elif current_room.name == "Kitchen" and command == "CUPBOARD":
        # Open kitchen.cupboard and concat each of the contents to the end of room_items
        current_room.room_items += kitchen.cupboard.open()
    # Can only open cabinet if holding a flashlight that isOn
    elif current_room.name == "Kitchen" and command == "CABINET" and (("red flashlight" in heldItems and redFlashlight.isOn) or ("yellow flashlight" in heldItems and yellowFlashlight.isOn)):
        # Open kitchen.cabinet and concat each of the contents to the end of room_items
        print("You use the flashlight to look inside the cabinet.")
        current_room.room_items += kitchen.cabinet.open()
    elif current_room.name == "Kitchen" and command == "CABINET":
        print("You check the cabinet, but it's too dark to see if there is anything inside.")
    elif current_room.name == "Small Office" and command == "PACKAGE":
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        current_room.room_items += smalloffice.package.open()
    elif current_room.name == "Small Office" and command == "READ":
        print("POCCNR??? You can't read it. It's written is some strange Cyrillic script.")
    elif current_room.name == "Small Office" and command == "DESK" and "brass key" in heldItems:
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        print("You use the brass key to unlock the desk.")
        current_room.room_items += smalloffice.desk.open()
    elif current_room.name == "Small Office" and command == "DESK":
        print("The desk drawer is locked.")
    elif current_room.name == "Laboratory" and command == "SHELF":
        # Open lab.shelf and concat each of the contents to the end of room_items
        current_room.room_items += lab.shelf.open()
    elif current_room.name == "Library" and command == "DESK":
        current_room.room_items += library.desk.open()
    elif current_room.name == "Library" and command == "SHELF":
        current_room.room_items += library.shelf.open()
    elif current_room.name == "Water storage" and command == "CABINET":
        current_room.room_items += waterstorage.cabinet.open()
    elif current_room.name == "Water storage" and command == "CANS":
        current_room.room_items += waterstorage.can.open()
    elif current_room.name == "bathroom" and command == "SHELF":
        # Open kitchen.cupboard and concat each of the contents to the end of room_items
        current_room.room_items += bathroom.shelf.open()
    elif current_room.name == "bathroom" and command == "CABINET":
        # Open kitchen.cupboard and concat each of the contents to the end of room_items
        current_room.room_items += bathroom.cabinet.open()

    # ********************************* MOVE *********************************
    else:
        current_room = current_room.move(command,visitedRooms) # If it was none of those commands, assume it was a direction. Try to move.
    return current_room


#THE LOOP
while True:
    print("\n")
    # Print current room info
    myHealth = current_room.info(heldItems,myHealth,visitedRooms) # this returns myHealth cuz an enemy in the room could hurt you
    if myHealth <= 0:
        print("You died.\nGAME OVER")
        break
    # Print player items
    playerItems()
    # Get user input
    command = input("> ")
    # Check the user input
    current_room = checkUserInput(current_room,command,heldItems)
