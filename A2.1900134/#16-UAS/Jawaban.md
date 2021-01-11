1.Apa itu class?
Class adalah salah satu cara bagaimana kita membuat sebuah kode yang mempunyai behaviour tertentu dan lebih mudah dalam mengorganisasi berbagai fungsi dan state-nya.
2.Apa itu Instance?
Instance adalah istilah lain dari objek suatu kelas.
3.Apa hubugan antara class dan instance?
Hubungan antara class dengan instance ialah instance merupakan bagian dari class, dan class biasanya memiliki beberapa instance.
4.Apa syntax python yang digunakan untuk menentukan class baru?
class Nama_class:
5.Apa konvensi ejaan untuk nama class?
Diawali dengan huruf besar, mewakili objek yang sesuai, tidak mengandung istilah koding.
6.Bagaimana anda memberikan instantiate, atau membuat instance dari sebuah class?
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
7.Bagaimana anda mengakses atribut dan perilaku instance class?
dengan membuat kode metode seperti berikut:
class hero: #template
    #class variabel
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
8.apa itu metode?
Metode didefinisikan di dalam class dan digunakan untuk mendapatkan isi sebuah instance. Mereka juga bisa digunakan untuk melakukan operasi dengan atribut objek.
9.Apa tujuannya self?
Saat Anda membuat instance baru dari class, Python secara otomatis menentukan apa self itu dan meneruskannya ke __init__metode ini.
10.Apa tujuan dari __init__metode ini?
untuk menginisialisasi (misalnya, tentukan) atribut awal objek dengan memberi mereka nilai default (atau side state). Metode ini harus memiliki setidaknya satu argumen dan juga selfvariabel, yang mengacu pada objek itu sendiri.