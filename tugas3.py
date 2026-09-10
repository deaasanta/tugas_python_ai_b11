# tugas 3 python basics
# nama : Dea Santa Nainggolan
# kelas : AI

# 1. variabel dan tipe data
nama = "Santa"
umur = 22
tinggi_badan = 155.5
sudah_kuliah = True
hobi = ["membaca", "olahraga", "coding", "nonton film", "gaming"]

print("1. Variabel dan Tipe Data")
print("Nama :", nama, type(nama))
print("Umur :", umur, type(umur))
print("Tinggi badan :", tinggi_badan, type(tinggi_badan))
print("Status kuliah :", sudah_kuliah, type(sudah_kuliah))
print("Hobi :", hobi, type(hobi))
print()

# 2. manipulasi string
print("2. Manipulasi String")
kata1 = "Halo"
kata2 = "Dunia"
gabung = kata1 + " " + kata2
print("Gabungan :", gabung)
print("Panjang string :", len(gabung))
print("Upper :", gabung.upper())
print("Lower :", gabung.lower())
print()

# 3. operasi matematika
print("3. Operasi Matematika")
a = 15
b = 4
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print()

# 4. list dan akses elemen
print("4. List dan Akses Elemen")
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
print("list awal :", buah)
print("elemen ke 1 :", buah[0])
print("elemen ke 3 :", buah[2])

buah.append("semangka")
print("setelah append :", buah)

buah.remove("jeruk")
print("setelah remove jeruk :", buah)

hapus = buah.pop()
print("item yang dihapus pop() :", hapus)
print("list sekarang :", buah)
print()

# 5. input dari user
print("5. Input dari User")
nama_user = input("masukkan nama kamu : ")
umur_user = input("masukkan umur kamu : ")

print("Halo, nama saya " + nama_user + " dan umur saya " + umur_user + " tahun.")