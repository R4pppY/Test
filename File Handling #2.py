# #fungsi sebuah file

# #cara 1 
# with open("dokumen.txt","w") as file:
#     file.write("Saya menulis kedalam dokumen.txt")


# #cara 2 
# file2 = open("dokumen2.docx","w")
# file2.write("ini adalah dokumen2")


#membaca sebuah file

# cara 1
with open("dokumen.txt","r") as file:
    hasil = file.read()
    print(hasil)

with open("dokumen.txt","r") as file:
    hasil = file.readline()
    print(hasil)

with open("dokumen.txt","r") as file:
    hasil = file.readlines()
    print(hasil)

# cara 2

file = open("dokumen2.docx")
hasil = file.read()

