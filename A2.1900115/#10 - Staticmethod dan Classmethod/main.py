class Hero:
    #private class veriabel
    __jumlah = 0;
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
    #methode ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    #method ini hanya berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    #method static (decorete) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper =Hero ('seniper')
print(Hero.getJumlah2())
rikamaru = Hero ('rikamaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print (Hero.getJumlah3())