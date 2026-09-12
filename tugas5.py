# tugas 5 python function and class
# nama : Dea Santa Nainggolan Parhusip
# kelas : AI


def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"

    def __str__(self):
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


if __name__ == "__main__":
    print("FUNCTIONS")
    print(greet("Dea"))
    print(f"tambah(5, 7) = {tambah(5, 7)}")
    print(f"tambah(10) = {tambah(10)}")
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([]) = {rata_rata([])}")

    print("\nCLASS STUDENT")
    mhs1 = Student("Dea", "A123")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(82)

    mhs2 = Student("Santa", "A456")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(65)
    mhs2.tambah_nilai(58)

    print(mhs1)
    print(f"Rata-rata {mhs1.nama}: {mhs1.rata_nilai()} - Status: {mhs1.status()}")

    print(mhs2)
    print(f"Rata-rata {mhs2.nama}: {mhs2.rata_nilai()} - Status: {mhs2.status()}")