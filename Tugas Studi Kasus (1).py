"""
Cetak: Gunakan fungsi input
Kode Matakuliah: IF1152
Nama Matakuliah: Bahasa Inggris
Nilai UTS: 95
Nilai UAS: 90
Nilai Praktikum: 85
Nilai Aktifitas: 80
Nilai Proyek: 95
Total Nilai: 
Nilai Huruf: A
"""
# Keterangan Total Nilai
# UTS - 20%, UAS - 20%, Praktikum - 10%, Aktifitas: 20%, Proyek 30%

#Total Nilai = %UTS + %UAS + %PR + %AK + %PRO
#Total Nilai = 

#Nilai Huruf:
#90 - 100 : A
#80 - 90 : B
#70 - 80 : C
#60 - 70 : D
#50 - 60 : E
#<50 : F

kodematkul =input("Masukkan Kode mata kuliah :")
print(kodematkul)
namaMatkul =input("Masukkan nama mata kuliah :")
print(namaMatkul)

NilaiUTS=int(input("masukin nilai uts anda:"))
NilaiUAS=int(input("masukin nilai uas:"))
NilaiPraktikum=int(input("masukin nilai praktikum:"))
NilaiAktifitas=int(input("masukin nilai aktifitas:"))
NilaiProyek=int(input("masukin nilai proyek:"))
totalNilai=(NilaiUTS *20/100)+(NilaiUAS *20/100)+(NilaiPraktikum *10/100)+(NilaiAktifitas *20/100)+(NilaiProyek *30/100)
print(totalNilai)
print(NilaiUTS)
print(NilaiUAS)
print(NilaiPraktikum)
print(NilaiAktifitas)
print(NilaiProyek)

if totalNilai >= 90 and 100:
   print("dapat A")
elif totalNilai >=80 and totalNilai <90:
   print("dapat B")
elif totalNilai >=70 and totalNilai <80:
  print("dapat C")
elif totalNilai >=60 and totalNilai <70:
  print("dapat D")
elif totalNilai >=50 and totalNilai <60:
  print("dapat E")


