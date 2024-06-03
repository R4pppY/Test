# Kalkulator Sederhana

# Fungsi untuk penambahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y == 0:
        return "Tidak bisa membagi dengan nol"
    return x / y

# Menampilkan menu operasi
print("Pilih operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input dari user
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Meminta input bilangan
angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))

# Memproses operasi sesuai pilihan
if pilihan == '1':
    print("Hasil penambahan:", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil pengurangan:", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil perkalian:", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil pembagian:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid")

