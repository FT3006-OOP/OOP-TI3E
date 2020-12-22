class hero :

    def __init__(self,name,health):
        self.name = name
        self.health = health

class hero_intellegent(hero):
    pass

class hero_strength(hero):
    pass

lina = hero('lina',100)
techies = hero_intellegent('techies',50)
axe = hero_strength('axe',200)

print(lina.name)
print(techies.name)
print(axe.name)
