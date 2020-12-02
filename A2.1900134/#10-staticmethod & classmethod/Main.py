class hero:

    #private class variable
    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        hero.__jumlah += 1

    #method ini hanya berlaku untuk objek
    def getJumlah(self):
        return hero.__jumlah

    #method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return hero.__jumlah

    #method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper = hero('sniper')
print(hero.getJumlah2())
rikimaru = hero('rikimaru')
print(sniper.getJumlah2())
drawranger = hero('drawranger')
print(hero.getJumlah3())
