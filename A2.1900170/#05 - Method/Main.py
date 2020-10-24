class Hero:
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):

        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1


    def siapa(self):
        print("namaku adalah " + self.name)


    def healthup(self,up):
        self.health += up


    def getHealth(self):
        return self.health


hero1  = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

hero1.siapa()
hero1.healthup(10)

print(hero1.getHealth())