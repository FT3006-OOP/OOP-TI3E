class   Hero:

    def __init__(self,name,healt,attackPower,armorNumber):
        self.name = name
        self.healt = healt
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name )
        lawan.diserang(self, self.attackPower):
    def diserang(self. lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ' str(attack_diterima))
        self.healt -= attack_diterima
        print('darah ' + self.name ' tersisa ' + str(self.healt))

        sniper = Hero('sniper',100,10,5)
        rikimaru = Hero('rikimaru',100,20,10)

        sniper.serang(rikimaru)
        print("\n")
        rikimaru.serang(sniper)
        print("\n")
        rikimaru.serang(sniper)
        print("\n")
        rikimaru.serang(sniper)
        print("\n")
        rikimaru.serang(sniper)
        
