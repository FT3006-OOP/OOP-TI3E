class Hero: #template
    #ini adalah varibel calass
    jumlah = 0
    def __init__(self, inputname, inputHealt, inputPower, inputArmor):
        self.nama = inputname
        self.healt = inputHealt
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuaat Hero Dengan Nama" + inputname)


hero1 = Hero('sniper', 100, 10, 4)
print (Hero.jumlah)
hero2 = Hero('maria', 100, 15, 1)
print (Hero.jumlah)
hero3 = Hero('ucup', 1000, 10, 0)
print (Hero.jumlah)

