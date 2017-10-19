class Phone():
    def __init__(self,color,batteries,deadBattery):
        self.color = color 
        self.phonebattery = batteries 
        self.deadBatter = deadBatter
        self.On = False

    def get_interface(self,heldItems,current_room):
        if self.On and not self.deadBatter:
            print("The Phone is switched on and dialing 911 will be there when place is clear. You can TURN Phone OFF")
        elif self.On and self.deadBatter:
            print("The Phone is switched on but its not working. You can TURN Phone OFF")
        else:
            print("The Phone is switched off. You can TURN Phone ON")
        if self.phonebattery == 0 and "battery" in heldItems:
            print("You can ADD BATTERY TO Phone")
        if self.phonebattery > 0:
            print("You can REMOVE Phone BATTERY")

    def check_input(self,command,heldItems,current_room):
        if command == "TURN Phone OFF":
            self.turn_off()
        if command == "TURN Phone ON":
            self.turn_on()
        if command == "ADD BATTERY TO Phone" and self.phonebattery == 0 and "battery" in heldItems:
            self.add_batteries(heldItems)
        if command == "REMOVE Phone BATTERY" and self.phonebattery == 1:
            self.remove_batteries(heldItems,current_room)

    #setter that removes 1 battery if there are batteries in the flashlight
    #returns 1 if successful, to add 1 battery to room
    def remove_batteries(self,heldItems,current_room):
        if self.batteries > 0:
            self.batteries -= 1
            if self.deadBattery:
                print("You remove 1 dead battery from the Phone.")
                current_room.room_items.append("dead battery")
            else:
                print("You remove 1 good battery from the Phone.")
                current_room.room_items.append("battery")
        else:
            print("There aren't any batteries in the Phone.")
