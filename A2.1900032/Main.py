class Hero: #template
    pass


hero1 = Hero() #Object / instance
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 100

hero3.name = "ucup"
hero3.health =100

print(hero1)
print(hero1.__dict__)
print(hero1.name)