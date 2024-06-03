#Kamus Pyton {} kunci/key:nilai/value | kunci identik

pemrograman = {"namaMK":"pemrograman", "sks":4, "nilai":99}

#merubah nilai
pemrograman
pemrograman["nilai"] = "99"

#menambah data baru 
pemrograman
pemrograman["huruf"] = "A"

#Cara mengakses nilai / value menggunakan kunci/key 
print(pemrograman["nilai"])
print(pemrograman["huruf"])
print(pemrograman)


#menghapus 1 data 
del pemrograman["huruf"]
print(pemrograman)

#menghapus semua data 
# pemrograman.clear()
# print(pemrograman)

#mengintegrasikan kamus dengan list
matematika = {"namaMK":"Matematika", "sks":2, "nilai":88} 

matakuliah = [pemrograman,matematika]
print(matakuliah[0]["nilai"]) #99

matematika = {"namaMK":"Matematika", "sks":2, "nilai":88} 

matakuliah = [pemrograman,matematika]
print(matakuliah[1]["nilai"]) #80