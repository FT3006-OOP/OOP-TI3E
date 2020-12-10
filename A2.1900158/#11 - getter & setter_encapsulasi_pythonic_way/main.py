class Hero:

    def __init__(self,name,health,armor):
      
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.__info = "name{} : \n\thealth: {}".format(self.__name,self.__health)

    @property
    def info (self):
        return "name{} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor (self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor (self, input):
        self.__armor = input

    @armor.deleter
    def armor (self):
        print ("armor di delet")
        self.__armor = None


print("merubah info")
seniper = Hero("seniper", 100,10)
print (seniper.info)
seniper.name ='dadang'
print (seniper.info)


print("getter and setter untuk armor: ")
print(seniper.armor)

seniper.armor=50
print (seniper.armor)

print ("delet armor")
del seniper.armor
print (seniper.__dict__)
