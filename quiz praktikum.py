def penjumlahan2bil():
    a = int(input("masukkan bilangan pertama : "))
    b = int(input("masukkan bilangan kedua : "))
    print(a+b)
    
def pengurangan2bil():
    a = int(input("masukkan bilangan pertama : "))
    b = int(input("masukkan bilangan kedua : "))
    print(a-b)

def perkalian2bil():
    a = int(input("masukkan bilangan pertama : "))
    b = int(input("masukkan bilangan kedua : "))
    print(a*b)

def pembagian2bil():
    a = int(input("masukkan bilangan pertama : "))
    b = int(input("masukkan bilangan kedua : "))
    print(a/b)   
     
print("menu")
print("1.   penjumlahan")
print("2.   pengurangan")
print("3.   perkalian")
print("4.   pembagian")
userinput = input("pilih menu : ")
if userinput =='1':
    penjumlahan2bil()
elif userinput =='2':
    pengurangan2bil()
elif userinput == '3':
    perkalian2bil()
elif userinput =='4':
    pembagian2bil()

