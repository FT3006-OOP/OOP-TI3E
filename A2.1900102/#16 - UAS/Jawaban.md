1. Class adalah prototipe yang ditentukan pengguna untuk objek yang mendefinisikan seperangkat atribut yang menjadi ciri objek kelas apa pun.
2. Instance adalah objek individu dari kelas tertentu. Obyek yang termasuk dalam Lingkaran kelas, misalnya adalah turunan dari Lingkaran kelas. Instance bisa juga disebut sebagai wujud dari class.
3. Hubungan class dan instance yaitu class adalah rancangan atau blue print dari sebuah objek. Sedangkan objek adalah sebuah variabel yang merupakan instance atau perwujudan dari class. Instance bisa diartikan sebagai wujud dari class.
4. class NamaClass:
5. Konvensi ejaan untuk nama class yaitu diawali dengan huruf kapital.
6. Memberi instance, atau membuat instance dari sebuah class yaitu ketikan sintak berikut yang diakhiri tanda baca titik koma : NamaClass namaObj = new NamaClass(); Kata kunci new berfungsi untuk membuat objek baru dari class tertentu.
7. Mengakses atribut dan perilaku instance class yaitu dengan menggunakan tanda titik (.), contohnya namaObj.namaMethod(); namaObj.atribut1;
8. Metode adalah fungsi-fungsi yang ada didalam class.
9. Fungsi self adalah sebagai sebuah variabel yang menyatakan kelas itu sendiri. Misalnya kita ingin memanggil sebuah variable atau method di dalam sebuah kelas(class) dan method yang akan kita panggil ada di dalam kelas itu juga, maka kata self akan digunakan di depan variabel atau methodnya. Contohnya : def __init__(self,name,health):
        self.name = name
        self.health = health
10. Method __init__() berguna untuk melakukan inisialisasi pembuatan object dari class.