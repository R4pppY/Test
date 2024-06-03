# File

# Buat File
file = open("Daftar-Belanja.txt", "w")
file.write("Daftar Belanja Ibu: ")
file.write("\n1, Cabai")
file.write("\n2, Bawang")
file.write("\n3, Garam")
file.close()

# Update File Tanpa Hapus Isi File
file = open("Daftar-Belanja.txt", "a")
file.write("\n4, Tepung")
file.close()

# Baca File di Terminal
file = open("Daftar-Belanja.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.read(10)) # Membaca 10 karakter saja
# print(file.readlines())
file.close()

# Menghapus isi file
file = open("Daftar-Belanja.txt", "w")
file.close()

# Hapus File
import os
os.remove("Daftar-Belanja.txt")