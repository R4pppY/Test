
anggota = []

while True:
    print("Program pencacatan anggota UKM")
    print("1. Cetak daftar anggota")
    print("2. Tambah anggota")
    print("3. Hapus anggota")
    print("4. Cek status anggota")
    print("5. Keluar")

    pilihan = input ("Masukan pilihan: ")

    if pilihan == "1":
        print("Daftar anggota:")
        for nama in anggota:
            print(nama)
    elif pilihan == "2":
        nama = input ("Masukan nama: ")
        anggota.append(nama)
        print("Anggota berhasil ditambahkan")
    elif pilihan == "3":
        nama == input("Masukan nama yang ingin dihapus")
        del anggota [anggota.index(nama)]
    elif pilihan == "4":
        break
