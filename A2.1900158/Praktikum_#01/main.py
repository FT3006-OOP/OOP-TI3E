class hero: # namanya class 
    pass


hero1 = hero() # kalo ini objek
hero2 = hero()
hero3 = hero()


hero1.nama = "seniper"
hero1.health = 100

hero2.nama = "seven"
hero2.health = 200

hero3.nama = "ucup"
hero3.health= 1000
print(hero1)
print(hero1.__dict__)
print(hero1.nama)