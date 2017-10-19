class Sniper():
    def __init__(self,color,maxAmmo,currentAmmo):
        self.colour= color #red,orange, ect
        self.maxAmmo= maxAmmo
        self.currentAmmo= currentAmmo
        self.isOn=True


    def remove_ammo(self,heldItems,current_room):
        if self.currrentAmmo > 1:
            self.currentAmmo -=1
            if self.currentAmmo:
                print("You remove 1 ammo from the "+self.colour+" sniper.")
                current_room.room_items.append("empty ammo")



    def add_ammo(self,heldItems):
        if self.currentAmmo < 3 and "1 ammo" in heldItems:
            self.currentAmmo +=1
            print("You put 1 ammo in the "+self.colour+" sniper rifle.")
            heldItems.remove("1 ammo")
            self.maxAmmo=currentAmmo+1
        elif self.currentAmmo > 3:
            print("The "+self.colour+" sniper rifle already has enough ammo")
        elif not "1 ammo" in heldItems:
            print("You aren't holding 1 ammo")




        def get_state(self,heldItems,current_room):
            if self.isOn and self.currentAmmo > 0:
                print("The "+self.colour+" sniper is switched on and ready to fire. You can TURN "+self.color.upper()+" SNIPER OFF")
            elif self.isOn and self.currentAmmo==0:
                print("The "+self.colour+" sniper is switched on but its not working. You can TURN "+self.color.upper()+" SNIPER OFF")
            else:
                print("The "+self.colour+" sniper is switched off. You can TURN "+self.color.upper()+" SNIPER  ON")


        def get_interface(self,heldItems,current_room):
            
            if self.currentAmmo == 0 and "1 ammo" in heldItems:
                print("You can ADD 1 AMMO TO "+self.colour.upper()+" SNIPER")
            if self.batteries > 0:
                print("You can REMOVE "+self.colour.upper()+" SNIPER's AMMO")

            
            
