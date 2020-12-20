class Hero:
     def __init__(self, name, health):
         self.name = name
         self.health = health

class Hero_intelegen(Hero):
    pass

class Hero_strangeth(Hero):
    pass

lina = Hero ('Lina',100)
teachies = Hero_intelegen('teachieas',50)
axe = Hero_strangeth('axe', 200)

print (lina.name)
print (teachies.name)
print (axe.name)
