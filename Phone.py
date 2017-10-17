class phone():
    def __init__(self,color,batteries,deadBattery):
        self.colo = color 
    self.batteries = batteries 
    self.deadBatter = deadBatter
    self.On = False

def get_interface(self,heldItems,current_room):
    if self.On and not self.deadBatter:
        print("The "+self.colo+" Phone is switched on and dialing 911 will be there when place is clear. You can TURN "+self.colo.upper()+" Phone OFF")
    elif self.On and self.deadBatter:
        print("The "+self.colo+" Phone is switched on but its not working. You can TURN "+self.colo.upper()+" Phone OFF")
    else:
        print("The "+self.colo+" flashlight is switched off. You can TURN "+self.colo.upper()+" Phone ON")
    if self.batteries == 0 and "battery" in heldItems:
        print("You can ADD BATTERY TO "+self.colo.upper()+" Phone")
    if self.batteries > 0:
        print("You can REMOVE "+self.color.upper()+" Phone BATTERY")
