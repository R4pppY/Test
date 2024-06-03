#Studi Kasus Nilai

def nilaiMK ():
    uts = int(input("Silahkan masukkan nilai uts:"))
    uas = int(input("Silahkan masukkan nilai uas:"))
    partisipasi = int(input("Silahkan masukkan nilai partisipasi:"))
    proyek = int(input("Silahkan masukkan nilai proyek:"))
    #bobot / presentase
    b_uts = uts * 25 / 100
    b_uas = uas * 25 / 100
    b_partisipasi = partisipasi * 20 / 100
    b_proyek = proyek * 30 / 100

    #nilai total
    nilaiTotal = b_uts + b_uas + b_partisipasi + b_proyek
    print(nilaiTotal)
    return nilaiTotal

hasilfungsi = nilaiMK()

if hasilfungsi > 80:
   nilaiHuruf = "A"
elif hasilfungsi > 70:
   nilaiHuruf = "B"
else:
   nilaiHuruf = "C"

print(nilaiHuruf)
