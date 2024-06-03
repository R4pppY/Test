dataMhs = [{"Nama":"Nama","Nim":"Nim","Jurusan":"Jurusan"},{"Nama":"Rafi Muhammad Akbar","Nim":"1152700017","Jurusan":"Informatika"}]

print(type(dataMhs[0]))

print(dataMhs[1]["Nim"])

#Fungsi Menulis File
def menulisFile(linkFile,data):
    with open(linkFile,'w') as file:
        for Mhs in data:
            stringMhs = f"{Mhs['Nama']},{Mhs['Nim']},{Mhs['Jurusan']}\n"
            print(stringMhs)
            file.write(stringMhs)

menulisFile('mhs.csv',dataMhs)
print("data berhasil ditulis kedalam sebuah file")

