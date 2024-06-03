# def cetak_daftar(daftar):
#     for nama in daftar:
#         print("Nama saya: ", nama)

# daftar_nama = ["Andi", "Budi", "Caca"]
# cetak_daftar(daftar_nama)

# def cetak_daftar(daftar):
#     for nama in daftar:
#         if "e" in nama:
#             print("Nama saya: ", nama)

# daftar_nama = ["Andi", "Emire", "Caca"]
# cetak_daftar(daftar_nama)

def cetak_daftar(daftar):
    for nama in daftar:
        print("Nama saya: ", nama)

daftar_nama = ["Andi", "Emire", "Caca"]
daftar_nama.append ("Kuncoro")

cetak_daftar(daftar_nama)

del daftar_nama[0]

def cek_status(nama,daftar):
    if nama in daftar:
        print(nama, "ada di dalam list")
    else:
        print(nama, "tidak ada di dalam list")


user_input = input("Masukan Nama : ")
cek_status(user_input, daftar_nama)

print(daftar_nama)


def cetak_semua(daftar):
    for item in daftar:
        print(item)