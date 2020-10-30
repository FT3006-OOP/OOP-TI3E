class Hero:
    #class variabel
    jumlah = 0
    def __init__(self, inputname, inputHealth, inputPower, inputArmor) :
        self.name = inputname
        self.Health = inputHealth
        self.Power = inputPower
        self.Armor = inputArmor
        Hero.jumlah += 1
    #voind fanction, method tanpa return
    def siapa(self):
        print("namaku adalah "+ self.name)
    #methode dengan argumen
    def healtup(self, up):
        self.Health += up
    def getheath(self):
        return self.Health

hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario beros', 90, 5, 10)

print (hero1.__dict__)
hero1.siapa()

hero1.healtup(10)
print(hero1.__dict__)

print(hero1.getheath())