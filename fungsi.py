print("belajar materi fungsi")
#review sintaks
#def nama fungsi (parameter):

#void function (fungsi kosong)
def tambah1000 (uang):
    """ini adalah fungsi tambah 1000"""
    uang += 1000
    print("Uang saya setelah ditambah 1000", uang)

tambah1000(2000)

#return function
def tambah5000 (uang):
    """ini adalah fungsi tambah 5000"""
    uang += 5000
    print("Uang saya setelah ditambah 5000", uang)
    return uang

returnNilai = tambah5000(5000)
print(returnNilai)

#return function non argumen
def tambah2000 ():
    """ini adalah fungsi tambah 2000"""
    #memanfaatkan fungsi input
    uang = int(input("Masukkan uang yang akan di + 2000:"))
    uang += 2000
    print("Uang saya setelah ditambah 2000", uang)
    return uang

hasilFungsiNA = tambah2000()

