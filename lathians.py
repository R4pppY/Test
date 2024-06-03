pilihanMatkul = input("silahkan masukan kode matakuliah:")
print(pilihanMatkul)
pilihanMatkul = input("silahkan masukan nama matakuliah:")
print(pilihanMatkul)

nilaiuts=int(input("masukin nilai uts anda:"))
nilaiuas=int(input("masukin nilai uas:"))
nilaipraktikum=int(input("masukin nilai praktikum:"))
nilaiaktifitas=int(input("masukin nilai aktifitas:"))
nilaiproyek=int(input("masukin nilai proyek:"))
totalnilai=(nilaiuts *20/100)+(nilaiuas *20/100)+(nilaipraktikum *10/100)+(nilaiaktifitas *20/100)+(nilaiproyek *30/100)
print(totalnilai)
print(nilaipraktikum)
print(nilaiuas)
print(nilaiproyek)
print(nilaiuts)
print(nilaiaktifitas)
if totalnilai >= 90 and 100:
   print("dapetnya A")
elif totalnilai >=80 and totalnilai <90:
   print("dapetnya B")
elif totalnilai >=70 and totalnilai <80:
  print("dapetnya C")
elif totalnilai >=60 and totalnilai <70:
  print("dapetnya D")
elif totalnilai >=50 and totalnilai <60:
  print("dapetnya E")
