# #Perulangan dan kamus

# #List
# dompet = [5000,10000,20000,50000]

# #Perulangan
# #for variable in sequence
# #sequence: list,string, tuple
# #sequence: elemennya bisa diakses menggunakan indeks

# for i in dompet:
#     print(i)

# #string
# nama = "Rafi Muhammad Akbar"
# print(nama[0]) #R

# for ch in nama:
#     print(ch)

#while
#inisialisasi variabel n
# n = 0
# while(n<5):
#     print(n)
#     #tambah nilai n
#     n += 1

# while(True):
#     print("Rafi Muhammad Akbar")

#cara membedakan loopin for (sequence) dan while (incr)

#menggabungkan looping dan percabangan
# print(range(0,9))

# for i in range (0,9):
#     print(i)

# print(range(0,9))

# for i in range (0,9):
#     if i == 5:
#         continue
#     elif i == 7:
#         break
#     else:
#         print(i)

#mengkombinasikan looping, percabangan, input

# jumlahData = int(input("Masukkan jumlah data yang akan diinput"))

# #list untuk menampung data
# nama = []

# for i in range(jumlahData):
#     tambahNama = input("Masukkan nama yang akan ditambahkan:")
#     nama.append(tambahNama)

# print(nama)

# jumlahData = int(input("Masukkan jumlah data yang akan diinput"))

# #list untuk menampung data (2)
# nama = []

# for i in range(jumlahData):
#     tambahNama = input("Masukkan nama yang akan ditambahkan:")
#     nama.append(tambahNama)
#     if tambahNama == "Maiki":
#         break

# print(nama)

user = "Rafi"
password = 1152


while True:
    print("Daftar menu:")
    print("1.   Log in")
    print("2.   Input Data :")
    print("3.   Keluar:")

pilihanUser = input("Silahkan masukkan menu:")
while True:
    if pilihanUser == "1":
        u = input("Masukkan username anda:")
        p = int(input("Masukkan Password anda:"))
        if user == u and password == p:
            print("Berhasil masuk ke sistem")
    else:
        print("Masukkan akun dengan benar")











    