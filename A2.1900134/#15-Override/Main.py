class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class hero")
        print("{} health: {}".format(
            self.name,
            self.health
        )
    )


class Hero_intellegent(Hero):
    def __init__(self,name):
        super().__init__(name,100)

    #overide
    def showInfo(self):
        print("showInfo di subclass Hero_intellegent")
        print("{} \n\tTipe: intellegent, \n\thealth: {}".format(
            self.name,
            self.health
        )
    )


class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,200)


lina = Hero_intellegent('lina')
axe = Hero_strength('axe')

lina.showInfo()
