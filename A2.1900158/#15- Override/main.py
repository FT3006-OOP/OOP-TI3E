class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def showINfo(self):
        print("{} helath : {}".format(
            self.name,
            self.health)
            )

class Hero_inteLigent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
 
    def showINfo(self):
        print ('{} \n\tTipe : intelegent, \n\t heath : {}'.format(
            self.name,
            self.health
            )
            )

class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

lina = Hero_inteLigent('lina')
axe = Hero_strength('axe')

axe.showINfo()
