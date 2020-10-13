class Hero: #template
    def __init__(self, inputname, inputHealt, inputPower, inputArmor):
        self.nama = inputname
        self.healt = inputHealt
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero('sniper', 100, 10, 4)
hero2 = Hero('maria', 100, 15, 1)
hero3 = Hero('ucup', 1000, 10, 0)

print (hero1.__dict__)
print (hero2.__dict__)
print (hero3.__dict__)

