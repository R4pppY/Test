#buat sebuah kamus sederhana untuk menampilkan terjemahan
#dari bahasa inggris ke bahasa indonesia
#misal user menginput: i love you
#maka output akan menghasilkan saya cinta kamu
#nilai di dalam kamus tersebut tidak terdapat kata yang diinput
#maka inputan tersebut tidak bisa di terjemahkan

#misal: didalam kamus terdapat kata "i" dan "you"
#lalu user menginput: i love you
#maka outputnya adalah: saya love kamu

#tugasnya adalah inputan kalimat "i hate you" -> maka akan tampil -> saya hate kamu
kamus = {
    "i": "saya",
    "you": "kamu",
    "love": "cinta",
    "hate": "benci"
}

#input : "i love you" output -> saya cinta kamu
#input : "i hate you" output -> saya hate kamu

english = input("masukkan bahasa inggris")
splitENG = english.split(" ")
for i in splitENG:
    if i in kamus:
        print()