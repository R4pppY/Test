#Enkspsulasi

# Akses Modifier
# class Hero:
#     def __init__(self, nama, hp):
#         self.nama = nama
#         self.hp = hp
# class Hero_Status(Hero):
#     def __init__(self, nama):
#         super().__init__(nama, 100)

# Porsche = Hero_Status("Porsche")
# print(Porsche.nama, "dan", Porsche.hp)


# Protected
# class Hero:
#     def __init__(self, nama, hp, power):
#         self._nama = nama
#         self._hp = hp
#         self._power = power
#     def _buff(self, buff):
#         print("Total Power:", self._power + buff)
# class Hero_Status(Hero):
#     def __init__(self, nama, hp, power):
#         super().__init__(nama, hp, power)
#     def totalpower(self, debuff):
#         print("Total Power:", self._power - debuff)

# Zhilong = Hero("Zhilong", 100, 200)
# Zhilong._buff(300)
# Nana = Hero_Status("Nana", 100, 200)
# Nana._power = 200
# Nana.totalpower(100)

# Private
# class IF:
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim
#     def __cetak(self):
#         print(f"Nama Mahasiswa: {self.nama} dan NIM mahasiswa tsb adalah {self.__nim}")

# class IFA(IF):
#     def __init__(self, nama, nim):
#         super().__init__(nama, nim)

# Rafi = IFA("Rafi", 1152700017)
# print(f"Nama Saya: {Rafi.nama}")
# print(f"NIM Saya: {Rafi._IF__nim}")
# print(Rafi._IF__cetak())
    
# Setter dan Getter
# class IF:
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim
#     def pindah_kelas(self, nimBaru):
#         self.__nim = nimBaru
#     def show_nim(self):
#         return self.__nim
#     def cetak(self):
#         print(f"Nama Mahasiswa: {self.nama} dan NIM mahasiswa tsb adalah {self.__nim}")

# Guntur = IF("Guntur", 1152700017)
# Guntur.cetak()
# Guntur.pindah_kelas(1152700032)
# Guntur.cetak

# Statistic Method dan Class Method
class merkHP:
    __jumlah = 0 
    def __init__(self, nama):
        self.nama = nama
        merkHP.__jumlah += 1 
    @classmethod
    def showmerekhp(cls):
        print(f"merk hp: {cls.__name__}")
    @staticmethod
    def showJumlahHP():
        print(f"jumlah HP keseluruhan: {merkHP.__jumlah}")
class Xiaomi(merkHP):
    def __init__(self, nama):
        super().__init__(nama)
class Samsung(merkHP):
    def __init__(self, nama):
        super().__init__(nama)

Samsung_1 = Samsung("Samsung Galaxy A3")
Xiaomi_1 = Xiaomi("Redmi Note 10A")
merkHP.showJumlahHP()
Samsung.showmerekhp()
Xiaomi.showmerekhp()

        
    