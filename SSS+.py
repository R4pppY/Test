import math

class SegitigaSikuSiku:
    def _init_(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def keliling(self):
        sisi_miring = math.sqrt(self.alas*2 + self.tinggi*2)
        keliling = self.alas + self.tinggi + sisi_miring
        return keliling
    
    def luas(self):
        luas = (self.alas * self.tinggi) / 2
        return luas

# Contoh penggunaan:
segitiga = SegitigaSikuSiku(3, 4)
print("Keliling segitiga:", segitiga.keliling())
print("Luas segitiga:", segitiga.luas())