import math

class SegitigaSikuSiku:
    def __init__(self, alas, tinggi):
        self.a = alas
        self.t = tinggi

    def keliling(self):
        sisi_miring = math.sqrt(self.a**2 + self.t**2)
        keliling = self.a + self.t + sisi_miring
        return keliling
    
    def luas(self):
        luas = (self.a * self.t) / 2
        return luas

def main():
    segitiga = SegitigaSikuSiku(4, 7)
    print("Keliling segitiga siku-siku: ", segitiga.keliling())
    print("Luas segitiga siku-siku: ", segitiga.luas())

if __name__ == "__main__":
    main()