# Komentar dalam bahasa python
'''
Ini adalah komentar multiline
Penulis : Rafi Muhammad Akbar
Tanggal : 6 Oktober 2023
Mata Kuliah : Pemrograman Dasar
'''

# Review Materi Input, Output, Proses

# Output (Print)
print("Selamat datang di MK Pemrograman Dasar")

# Input
input("Masukan nama anda:")

# Proses - variable dan Tipe Data
print("Selamat datang di Sistem Informasi Akademik")

#variable - tipe data string - nama : username
username = "1152700019" 

#database user sistem infrasi akademik
username = "1152700017"
password = "114678"

print(username)
print(password)

user = input("masukan username anda:")
key = input("masukan password anda:")

# Percabangan - if elif else
# Operator Perbandingan == (sama dengan)

#cara 1 : nesting if (if bersarang)
if user == username :
    print(user == username) #True
    print("username anda sudah sesuai dengan database")
    if key == password:
        print(key == password) #True
        print("password anda sudah sesuai dengan database")
    else:
        print(key == password) #False
        print("username anda salah")
else:
    print(user == username) #False
    print("username anda salah")

#cara 2 : operator logika and, or, not, xor
if (user == username) and (key == password):
    print("username atau password anda tidak sesuai")
else:
    print("username atau password anda tidak sesuai")

# List -> tempat untuk menyimpan > 1 data
# Struktur data / tipe data List
# Cara membuat list menggunakan []

# menyimpan  4 data mahasiswa
listUsername =[1152700001,1152700003,1152700005,1152700007]
print(listUsername)

# Ada beberapa fungsi dalam list: len
# len = fungsi untuk mengetahui jumlah data pada list
print(len(listUsername)) #4

# Ada beberapa metode dalam list: extend, append
# extend, append = metode u/ menambah anggota dalam list
listUsername.append(1152700009) # + 1 anggota
listUsername.extend([1152700011,1152700013]) # > 1 anggota
print(listUsername)

#extend = sequence (list,string)

#akses element / anggota dalam list menggunakan indeks mulai 0
print(listUsername[0]) #mencetak 01

#akses juga bisa menggunakan indeks negatif nilai -1
print(listUsername[[-2]]) #mencetak 11

#list juga bisa bersarang
listUsername.append([1152700015,1152700017])
print(listUsername)
print(listUsername[-1][1])