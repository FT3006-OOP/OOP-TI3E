class Hero:
    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower


    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health


    def diserang(self,serangPower):
        self.__health -= serangPower

    def setAttpower(self,nilaibaru):
        self.__attPower = nilaibaru


earthshaker = Hero("eartshaker",50,5)


print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())  