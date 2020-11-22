class hero :
    def __init__(self,name,health,attackpower):
        self.__name = name
        self.__health = health
        self.__attpower = attackpower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    #setter

    def diserang(self,serangPower):
        self.__health -= serangPower

    def setAttpower(self,nilaibaru):
        self.__attpower = nilaibaru

#awal dari game
earthshaker = hero("earthshaker",50, 5)

# game berjalan
print(earthshaker.getName()) 
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())   