class Hero: # template
    pass


hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = "Diluc"
hero1.health = 100

hero2.name = "Venti"
hero2.health = 200

hero3.name = "Fischl"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)