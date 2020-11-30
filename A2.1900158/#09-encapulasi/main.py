class hero :
    def __init__(self,name,health,attackpower):
        self.__name= name
        self.__health = health
        self.__attackpower = attackpower
    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def diserang (self,serangPower):
        self.__health -= serangPower

# awal dari game
earthshaker = hero("eartShaker", 50, 5)


#game berjalan
print (earthshaker.getName())
print (earthshaker.getHealth())
earthshaker.diserang(5)
print (earthshaker.getHealth())