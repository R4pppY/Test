# ===============Penggunaan SQLite3 pada penggunaan database==================== #
import sqlite3
import random

# Membuat database
conn = sqlite3.connect('hoyoverse.db')
print("Database berhasil dibuat")

# Membuat table
conn.execute('''CREATE TABLE IF NOT EXISTS GENSHIN_IMPACT
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAMA TEXT NOT NULL,
            ELEMENTAL TEXT NOT NULL,
            SENJATA TEXT NOT NULL,
            BINTANG TEXT NOT NULL);''')

print("Table berhasil dibuat")

# Menambah data dengan input secara berulang dengan batasan nya di inputkan oleh user
def tambah_karakter():
    print("\n===== Tambah Karakter =====")
    banyak_data = int(input("Masukkan banyak data yang ingin di inputkan: "))
    for i in range(banyak_data):
        nama = input("Masukkan nama karakter: ").lower()
        elemental = input("Masukkan element karakter: ").lower()
        senjata = input("Masukkan senjata karakter: ").lower()
        bintang = input("Masukkan bintang karakter: ")
        if nama == "" or elemental == "" or senjata == "":
            print("Data tidak boleh kosong")
            break
        elif elemental != "pyro" and elemental != "hydro" and elemental != "anemo" and elemental != "electro" and elemental != "cryo" and elemental != "geo":
            print("Elemental tidak tersedia")
            break
        elif senjata != "sword" and senjata != "claymore" and senjata != "polearm" and senjata != "catalyst" and senjata != "bow":
            print("Senjata tidak tersedia")
            break
        elif bintang < "4" or bintang > "5":
            print("Bintang tidak boleh kurang dari 4 dan lebih dari 5")
            break
        conn.execute("INSERT INTO GENSHIN_IMPACT (NAMA, ELEMENTAL, SENJATA, BINTANG) VALUES (?, ?, ?, ?)", (nama, elemental, senjata, bintang))
        conn.commit()
        print("Data berhasil di inputkan")
        
# Menampilkan data
def tampilkan_karakter():
    print("\n===== Tampilkan Karakter =====")
    cursor = conn.execute("SELECT * FROM GENSHIN_IMPACT")
    for row in cursor:
        print("ID :", row[0])
        print("Nama :", row[1])
        print("Elemental :", row[2])
        print("Senjata :", row[3])
        print("Bintang :", row[4])
        print("====================================")

# Update data
def update_karakter():
    print("\n===== Update Karakter =====")
    id = input("Masukkan ID yang ingin di update: ")
    nama = input("Masukkan nama karakter: ").lower()
    elemental = input("Masukkan element karakter: ").lower()
    senjata = input("Masukkan senjata karakter: ").lower()
    bintang = input("Masukkan bintang karakter: ")
    if nama == "" or elemental == "" or senjata == "":
        print("Data tidak boleh kosong")
    elif elemental != "pyro" and elemental != "hydro" and elemental != "anemo" and elemental != "electro" and elemental != "cryo" and elemental != "geo":
        print("Elemental tidak tersedia")
    elif senjata != "sword" and senjata != "claymore" and senjata != "polearm" and senjata != "catalyst" and senjata != "bow":
        print("Senjata tidak tersedia")
    elif bintang != "4" or bintang != "5":
        print("Bintang tidak boleh kurang dari 4 dan lebih dari 5")
    conn.execute("UPDATE GENSHIN_IMPACT SET NAMA = ?, ELEMENTAL = ?, SENJATA = ?, BINTANG = ? WHERE ID = ?", (nama, elemental, senjata, bintang, id))
    conn.commit()
    print("\nData berhasil di update")

# Hapus data
def hapus_karakter():
    print("\n===== Hapus Karakter =====")
    id = input("Masukkan ID yang ingin di hapus: ")
    conn.execute("DELETE FROM GENSHIN_IMPACT WHERE ID = ?", (id))
    conn.commit()
    print("\nData berhasil di hapus")

# Cari data
def cari_karakter():
    print("\n===== Cari Karakter =====")
    nama = input("Masukkan nama karakter yang ingin di cari: ").lower()
    cursor = conn.execute("SELECT * FROM GENSHIN_IMPACT WHERE NAMA = ?", (nama,))
    print("\nHasil pencarian: ", nama)
    for row in cursor:
        print("ID :", row[0])
        print("Nama :", row[1])
        print("Elemental :", row[2])
        print("Senjata :", row[3])
        print("Bintang :", row[4])
        print("====================================")

def gacha_karakter():
    print("\n===== Gacha Karakter =====")
    cursor = conn.execute("SELECT * FROM GENSHIN_IMPACT")
    data = []
    for row in cursor:
        data.append(row)
    hasil = random.choice(data)
    print("Karakter yang anda dapatkan adalah: ")
    print("ID :", hasil[0])
    print("Nama :", hasil[1])
    print("Elemental :", hasil[2])
    print("Senjata :", hasil[3])
    print("Bintang :", hasil[4])
    print("====================================")
    
# Menu
def menu():
    while True:
        print("\n===== Selamat Datang Di Genshin Impact =====")
        print("1. Tambah karakter")
        print("2. Tampilkan karakter")
        print("3. Update karakter")
        print("4. Hapus karakter")
        print("5. Cari karakter")
        print("6. Gacha karakter")
        print("7. Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            tambah_karakter()
        elif pilihan == "2":
            tampilkan_karakter()
        elif pilihan == "3":
            update_karakter()
        elif pilihan == "4":
            hapus_karakter()
        elif pilihan == "5":
            cari_karakter()
        elif pilihan == "6":
            gacha_karakter()
        elif pilihan == "7":
            print("Terima kasih telah bermain Genshin Impact")
            conn.close()
            break
        else:
            print("Pilihan tidak tersedia")
        
menu()