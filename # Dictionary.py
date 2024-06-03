# Dictionary
# thisList = ["saya", "anda", "mereka"] #saya = 0, anda = 1, mereka = 2

thisDict = {
    "Merek" : "Mclaren",
    "Jenis" : "Mclaren 720S",
    "Tahun" : "2018",
    "Harga" : "9,2 Miliar"
} #key : value

print(thisDict["Merek"])
print(thisDict["Jenis"])
print(thisDict["Tahun"])
print(thisDict["Harga"])
print(len(thisDict))


# dictBaru = dict()
# dictBaru["Aku"] = "Kamu"
# dictBaru["Dia"] = "Mereka"

# print(dictBaru)


nilaiDict = {
    "Rafi" : [30,60,90,95,99,100],
    "Zaky" : [20,40,60,80,90,95]
}

print(nilaiDict["Rafi"])
print(nilaiDict['Zaky'])
print(nilaiDict["Rafi"][5])
print(nilaiDict['Zaky'][4])

print(type(nilaiDict))



dictProdi = {
    "Informatika" : {
        "Rapy" : {
            "Pemdas" : 99,
            "IlmuData" : 99
        },
        "Rafi" : {
            "Pemdas" : 100,
            "IlmuData" : 100
        },
        
    }
}

print(dictProdi["Informatika"]["Rafi"])


nilaiDict = {
    "Rafi" : [30,60,90,95,99,100],
    "Zaky" : [20,40,60,80,90,95]
}

total = 0
for item in nilaiDict["Rafi"]:
    total += item

print(total/len(nilaiDict["Rafi"]))

total = 0
for item in nilaiDict["Zaky"]:
    total += item

print(total/len(nilaiDict["Zaky"]))



luasWilayah = {
    "Bandug" : 139,
    "Padang" : 2100,
    "Tangerang" : 3140,
    "Serpong" : 1100
}
simpanKeys = luasWilayah.keys()
simpanValues = luasWilayah.values()

print(f"""ini method get keys() : {simpanKeys}, \n
      ini method get values() : {simpanValues}""")

print(type(simpanKeys))
print(type(simpanValues))

# luasWilayah["Serang"] = 4102

# print(luasWilayah)

# if "Tangerang" in luasWilayah:
#     print("Ya, Tangerang ada di luas wilayah")
# else:
#     print("TIDAK ADA")


luasWilayah2 = {
    "Jambi" : 11000,
    "Bali" : 12000
}
luasWilayah.update(luasWilayah2)
print(luasWilayah)


mahasiswa = {
    "mhs1" : "Rehan",
    "mhs2" : "Rafi",
    "mhs3" : "Danar",
    "mhs4" : "Dimas",
    "mhs5" : "Rifky"
}

for item in mahasiswa:
    print(item, " : ", mahasiswa[item])