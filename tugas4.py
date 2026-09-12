# tugas 4 struktur data python
# nama: Dea Santa Nainggolan
# kelas: AI

print("List akses dan manipulasi")

barang = ["Dea", 88, "Santa", 92, "Desan", 75]
print(barang)
print("elemen pertama", barang[0])
print("elemen terakhir", barang[-1])

print(barang[1:5:2])
print(barang[::-1])

print("sebelum", barang)
barang.append("Reza")
print("setelah append", barang)

barang.insert(1, "Nia")
print("setelah insert", barang)

barang.extend(["Doni", 100])
print("setelah extend", barang)

terambil = barang.pop()
print("pop", terambil, barang)

barang.remove("Santa")
print("setelah remove", barang)


print()
print("Tuple immutability dan unpacking")

bahasa = ("Python", "JavaScript", "Kotlin", "PHP", "Swift")
print(bahasa)
print("panjang", len(bahasa))
print(bahasa[0], bahasa[2])

satu, dua, *sisanya = bahasa
print(satu, dua, sisanya)

depan, *tengah, belakang = bahasa
print(depan, tengah, belakang)


print()
print("Set keunikan dan operasi himpunan")

hobi_saya = {"membaca", "olahraga", "coding", "musik"}
hobi_teman = {"coding", "musik", "gaming", "melukis"}

print(hobi_saya)
print(hobi_teman)
print("union", hobi_saya | hobi_teman)
print("intersection", hobi_saya & hobi_teman)
print("difference", hobi_saya - hobi_teman)
print("difference", hobi_teman - hobi_saya)
print("symmetric diff", hobi_saya ^ hobi_teman)

nilai = [80, 80, 90, 75, 90, 90, 75]
print("list awal", nilai)
print("jadi set", set(nilai))


print()
print("Dictionary key value dasar")

profil = {
    "nama": "Dea Santa Nainggolan",
    "nim": "4222301022",
    "angkatan": 2023,
    "kota": "Batam"
}
print(profil)

profil["prodi"] = "Teknologi Rekayasa Robotika"
print("tambah prodi", profil)

profil["kota"] = "Sidoarjo"
print("ubah kota", profil)

del profil["angkatan"]
print("hapus angkatan", profil)

print(profil.keys())
print(profil.values())
print(profil.items())

for key, val in profil.items():
    print(key, val)


print()
print("Nested structures")

koleksi_buku = [
    {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun": 2009},
    {"judul": "Ayat Ayat Cinta", "penulis": "Habiburrahman El Shirazy", "tahun": 2004},
    {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
    {"judul": "Sapiens", "penulis": "Yuval Noah Harari", "tahun": 2011},
    {"judul": "Laut Bercerita", "penulis": "Leila S Chudori", "tahun": 2017}
]

for buku in koleksi_buku:
    print(buku["judul"])

buku_baru = [b["judul"] for b in koleksi_buku if b["tahun"] >= 2010]
print("buku diatas tahun 2010", buku_baru)


print()
print("Comprehension dan utilitas")

deret = list(range(1, 21))

genap = [n for n in deret if n % 2 == 0]
print(genap)

kuadrat = [n**2 for n in deret]
print(kuadrat)

status = {n: "genap" if n % 2 == 0 else "ganjil" for n in range(1, 11)}
print(status)

kalimat = "Belajar struktur data di Python sangat menyenangkan"
huruf = {c.lower() for c in kalimat if c.isalpha()}
print(sorted(huruf))


print()
print("Keanggotaan dan pencarian sederhana")

if "gaming" in hobi_teman:
    print("gaming ada di hobi_teman")

if "berenang" not in hobi_saya:
    print("berenang tidak ada di hobi_saya")

target = "Desan"
if target in barang:
    print(target, "ditemukan di index", barang.index(target))
else:
    print(target, "tidak ditemukan")

cek = ["Dea", "Budi", "Nia", 100]
for item in cek:
    if item in barang:
        print(item, "ditemukan di index", barang.index(item))
    else:
        print(item, "tidak ditemukan")