class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter                    
    def diserang(self,serangPower):
        self.__health -= serangPower

    def setAttPower(self,nilaibaru):
        self.__attPower = nilaibaru

# awal dari game
earthshaker = Hero("earthshaker",5010,54)

#game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(63)
print(earthshaker.getHealth())