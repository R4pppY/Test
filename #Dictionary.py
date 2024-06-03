#Dictionary

# thisDict = {
#     "Nama" : "Rafi",
#     "Umur" : 18,
#     "Kelamin" : "Lk"
# }       #key : val


# for i in thisDict:
#     print(i, " : ", thisDict[i])

# print()

# for key, value in thisDict.items():
#     print(key, value)
    


thisDict = {
    "Merek" : "Mclaren",
    "Jenis" : "Mclaren 720S",
    "Tahun" : "2018",
    "Harga" : "9,2 Miliar"
}       #key : val


print(f"ini awal {thisDict}")
key1 = input("Masukkan Key : ")
val1 = input("Masukkan Value : ")

thisDict[key1] = val1
print(thisDict)




thisDictKosong = {}
while True:
    key1 = input("Masukkan Key : ")
    val1 = input("Masukkan Value : ")
    userInput = input("apakah data ingin diinput? [Y lanjut/N program stop]")
    if userInput == "N":
        break
    else:
        thisDictKosong[key1] = val1
        print(thisDictKosong)
    
print(thisDictKosong)