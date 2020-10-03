class Hero: # template
    pass


hero1 = Hero() # object
hero2 = Hero()
hero3 = Hero();

hero1.name = "Sniper"
hero1.health = 1000

hero2.name = "Kagura"
hero2.health = 1500

hero3.name = "Balmond"
hero3.health = 2500

print(hero1)
print(hero1.__dict__)
print(hero1.name)