class Hero: #template
    pass


hero1 = Hero() #object / instance
hero2 = Hero()
hero3 = Hero();

hero.name = "sniper"
hero.health = 100

hero2.name = "sven"
hero.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)