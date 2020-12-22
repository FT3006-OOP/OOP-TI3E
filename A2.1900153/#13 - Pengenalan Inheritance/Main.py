class Hero:
    
    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

Lina = Hero('Lina',100)
Techies = Hero_intelligent('Techies',50)
Axe = Hero_strength('Axe',200)

print(Lina.name)
print(Techies.name)
print(Axe.name)
