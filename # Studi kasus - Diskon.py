# # Studi kasus - Diskon 50%
# baju = 200000
# diskon = baju * 50 / 100
# bajuDiskon = baju -diskon
# print(bajuDiskon)

# # Studi kasus - Diskon 80%
# baju = 150000
# diskon = baju * 80 / 100
# bajuDiskon = baju -diskon
# print(bajuDiskon)

# Studi kasus - Diskon 50% + 40%
baju = 200000
diskon = baju *50/100
bajuDiskon = baju -diskon
diskon20 = bajuDiskon *40/100
bajuDiskon20 = bajuDiskon - diskon20
print("harga baju asli:",baju)
print("Harga baju setelah diskon (70 + 20):", bajuDiskon20)

diskonGab = (baju *50/100) + (baju *40/100)
bajuDiskonGab = baju - diskonGab
print("Harga baju setelah diskon (70 + 20) - Gabungan:", bajuDiskonGab)
