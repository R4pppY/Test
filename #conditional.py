#conditional

"""
ini belajar conditional

if
else
else if (elif)

IF SUATU KONDISI

ELSE IF

ELSE
"""

x = 5
y = 10

#if
if x> y:
    print(x, "lebih besar", y)
#else if
elif x == y:
    print(x, ("sama dengan"), y)
#else
else:
    print(x, "lebih kecil dari", y)



"""
and --- True True
or --- True False
not ---
"""


a = 10
b = 90
c = 20

# if a < b and b>c:
#   print("dua duanya benar")

#and nilai salah satunya harus true
if a > b or b > c or a > c:
    print("dua duanya benar")


str1 = "Aku sayang kamu"
str2 = "Aku sayang aku"

if str1 == str2:
    print("string sama")


print("iya") if a > b else print("tidak")

inputangka = int(input("masukan angka: "))
if inputangka % 2 == 0:
    print("genap") 
else :
    print("ganjil")

str3 = "abcdefghijklmnopqrstuvwxyz"
a =10
b = 20
print(str3[0])
if "a" in str3:
    print("ada")
    if a < b:
        print("a lebih besar")
    else:
        print("b lebih besar")