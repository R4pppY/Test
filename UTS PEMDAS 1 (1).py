# Fungsi untuk menghitung total nilai
def hitung_total_nilai():
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    praktikum = float(input("Masukkan nilai Praktikum: "))
    quiz = float(input("Masukkan nilai Quiz: "))
    partisipasi = float(input("Masukkan nilai Aktifitas Partisipasi: "))
    project = float(input("Masukkan nilai Hasil Project: "))
    
    total_nilai = 0.15 * uts + 0.20 * uas + 0.10 * praktikum + 0.05 * quiz + 0.15 * partisipasi + 0.35 * project
    return total_nilai

# Fungsi untuk menentukan nilai huruf
def nilai_huruf(total_nilai):
    if total_nilai >= 90:
        return 'A'
    elif total_nilai >= 80:
        return 'B'
    elif total_nilai >= 70:
        return 'C'
    elif total_nilai >= 60:
        return 'D'
    else:
        return 'E'

# Input jumlah mata kuliah
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

# Inisialisasi variabel untuk menghitung total SKS dan total nilai
total_sks = 0
total_nilai_sks = 0

# Membuat list untuk menyimpan data mata kuliah
mata_kuliah = []

# Loop untuk menginput data mata kuliah
for i in range(jumlah_mata_kuliah):
    print(f"Masukkan data untuk Mata Kuliah ke-{i + 1}:")
    nama_mata_kuliah = input("Nama Mata Kuliah: ")
    sks = int(input("SKS: "))
    nilai = hitung_total_nilai()
    nilai_h = nilai_huruf(nilai)
    
    if nilai_h != 'D' and nilai_h != 'E':
        total_sks += sks
        total_nilai_sks += nilai * sks
    
    mata_kuliah.append({
        'Nama Mata Kuliah': nama_mata_kuliah,
        'SKS': sks,
        'Nilai': nilai,
        'Nilai Huruf': nilai_h
    })

# Menghitung IPS
def hitung_ips(mata_kuliah):
    total_sks = 0
    total_nilai = 0

    for mk in mata_kuliah:
        sks = mk['sks']
        nilai = mk['nilai']

        if nilai in {'A', 'A-', 'A+', 'A/A'}:
            bobot_nilai = 4.0
        elif nilai in {'B', 'B-', 'B+', 'B/A'}:
            bobot_nilai = 3.0
        elif nilai in {'C', 'C-', 'C+', 'C/A'}:
            bobot_nilai = 2.0
        elif nilai in {'D', 'D-', 'D+', 'D/A'}:
            bobot_nilai = 1.0
        elif nilai in {'E', 'E-', 'E+', 'E/A'}:
            continue  # Mata kuliah dengan nilai E tidak dihitung

        total_sks += sks
        total_nilai += sks * bobot_nilai

    if total_sks > 0:
        ips = total_nilai / total_sks
    else:
        ips = 0.0

    return ips

# Contoh penggunaan fungsi hitung_ips
mata_kuliah = [
    {'nama': 'Pemrograman', 'sks': 4, 'nilai': 'A'},
    {'nama': 'Basis Data', 'sks': 3, 'nilai': 'A'},
    {'nama': 'Web', 'sks': 4, 'nilai': 'B'},
    {'nama': 'UI UX', 'sks': 3, 'nilai': 'B'},
    {'nama': 'Mobile', 'sks': 2, 'nilai': 'A'}
]

ips = hitung_ips(mata_kuliah)
print(f'IP semester: {ips:.2f}')

# Input jumlah semester
jumlah_semester = int(input("Masukkan jumlah semester: "))

# Menghitung IPK
total_ips = 0
for i in range(jumlah_semester):
    ips_semester = float(input(f"Masukkan IPS Semester {i + 1}: "))
    total_ips += ips_semester

ipk = total_ips / jumlah_semester

# Menampilkan IPK
print(f"IPK: {ipk:.2f}")