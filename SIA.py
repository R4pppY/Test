#koordinasi dengan modul yang lain (import)
import mahasiswa #import 1 modul
import dosen, matakuliah #import > 1 modul menggunakan ","
#untuk memanggil entitas (.)
print("data mahasiswa")
print(mahasiswa.nama)
print(mahasiswa.NIM)
print(mahasiswa.alamat)
print("\ndata dosen")
print(dosen.nama)
print("\ndata matakuliah")
print(matakuliah.nama)