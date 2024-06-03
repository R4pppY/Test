# ===============Penggunaan SQLite3 pada penggunaan database==================== #
import sqlite3

# Membuat database
conn = sqlite3.connect('IF23.db')
print("Database berhasil dibuat")

# Membuat table
conn.execute('''CREATE TABLE IF NOT EXISTS MAHASISWA_IF_A
            (NIM TEXT PRIMARY KEY,
            NAMA TEXT NOT NULL,
            UMUR INTEGER NOT NULL,
            ALAMAT TEXT NOT NULL);''')

print("Table Mahasiswa berhasil dibuat")

conn.execute('''CREATE TABLE IF NOT EXISTS DOSEN
            (NIDN TEXT PRIMARY KEY,
            NAMA TEXT NOT NULL,
            MATKUL TEXT NOT NULL);''')

def buat_mahasiswa():
    banyak_data = int(input("Masukkan banyak data yang ingin di inputkan: "))
    for i in range(banyak_data):
        nim = input("Masukan NIM mahasiswa: ")
        nama = input("Masukkan nama mahasiswa: ").lower()
        umur = int(input("Masukkan umur mahasiswa: "))
        alamat = input("Masukkan alamat mahasiswa: ").lower()
        if nim == "" or nama == "" or umur == "" or alamat == "":
            print("Data tidak boleh kosong")
            break
        elif umur < 15:
            print("Umur tidak boleh kurang dari 15 Tahun")
            break
        conn.execute("INSERT INTO MAHASISWA_IF_A (NIM, NAMA, UMUR, ALAMAT) VALUES (?, ?, ?, ?)", (nim, nama, umur, alamat))
        conn.commit()
        print("Data berhasil di inputkan")
        
def tampilkan_mahasiswa():
    cursor = conn.execute("SELECT * FROM MAHASISWA_IF_A")
    for row in cursor:
        print("NIM :", row[0])
        print("Nama :", row[1])
        print("Umur :", row[2])
        print("Alamat :", row[3])
        print("====================================")
        
def update_mahasiswa():
    nim = input("Masukkan NIM yang ingin di update: ")
    nama = input("Masukkan nama mahasiswa: ").lower()
    umur = int(input("Masukkan umur mahasiswa: ")).lower()
    alamat = input("Masukkan alamat mahasiswa: ").lower()
    if nim == "" or nama == "" or umur == "" or alamat == "":
        print("Data tidak boleh kosong")
    elif umur < 0:
        print("Umur tidak boleh kurang dari 0")
    conn.execute("UPDATE MAHASISWA_IF_A SET NAMA = ?, UMUR = ?, ALAMAT = ? WHERE NIM = ?", (nama, umur, alamat, nim))
    conn.commit()
    print("Data berhasil di update")
    
def hapus_mahasiswa():
    nim = input("Masukkan NIM yang ingin di hapus: ")
    conn.execute("DELETE FROM MAHASISWA_IF_A WHERE NIM = ?", (nim))
    conn.commit()
    print("Data berhasil di hapus")
    
def rata_rata():
    cursor = conn.execute("SELECT UMUR FROM MAHASISWA_IF_A")
    total_umur = 0
    i = 0
    for baris in cursor:
        total_umur += baris[0]
        i += 1    
    print(total_umur/i)

def menu():
    while True:
        print("===== Menu =====")
        print("1. Buat Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Update Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Rata-rata Umur")
        print("6. Exit")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            buat_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            update_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            rata_rata()
        elif pilihan == "6":
            conn.close()
            break
        else:
            print("Pilihan tidak tersedia")
        
menu()