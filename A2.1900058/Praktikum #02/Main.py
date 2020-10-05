class Hero : #template
    pass


hero1 = Hero() #object
hero2 = Hero()
hero3 = Hero();

hero1.name = "sniper"
hero1.health = 100

hero2.name = "hayabusa"
hero2.health = 200

hero3.name ="Silvana"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)