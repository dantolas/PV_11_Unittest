class Bottle:
    # 2 Konstrukotr (init)
    def __init__(self, capacity):

        if(capacity <= 0):
            raise Exception("Capacity must be a positive integer")        
        self.capacity = capacity
        self.volume = 0
        self.open = False
    # 3
    def setVolume(self,volume):

        if(self.open is False):
            raise Exception("bottle is closed")

        if(volume > self.capacity):
            raise Exception("Volume cannot be larger than bottle capacity.");

        self.volume = volume

    def getVolume(self):
        return self.volume
    # 4
    def clearBottle(self):

        if(self.open == False):
            raise Exception("bottle is closed")

        self.volume = 0
        return self.volume
    # 5
    def setVolumeMil(self,volumeInMil):

        if(self.open is False):
            raise Exception("bottle is closed")

        capacityInMil = self.capacity * 1000

        if (volumeInMil > capacityInMil):
            raise Exception("Capacity exceeded.");

    def getVolumeMil(self):
        return self.volume * 1000
    
    # 6 
    def changeState(self) :
        if(self.open is False):
            self.open = True
            return
        self.open = False
        



bottle = Bottle(36)

# print(bottle.capacity)
# print(bottle.volume)
# bottle.changeState()
# bottle.setVolume(20) 
# print(bottle.getVolume())
# bottle.setVolumeMil(6000)
# print(bottle.getVolumeMil())
# bottle.changeState()
# bottle.setVolume(10)


