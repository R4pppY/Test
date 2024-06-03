class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        pass

class Mamalia(Hewan):
    def __init__(self, nama, spesies):
        super().__init__(nama)
        self.spesies = spesies

    def menyusui(self):
        print(f"{self.nama} sedang memberi makan anaknya")

class Anjing(Mamalia):
    def __init__(self, nama, ras):
        super().__init__(nama, "Anjing")
        self.ras = ras

    def suara(self):
        return "Woof!"
    
    def gonggong(self):
        print(f"{self.nama} mengonggong: {self.suara()}")

class Kucing(Mamalia):
    def __init__(self, nama, ras):
        super().__init__(nama, "Kucing")
        self.ras = ras

    def suara(self):
        return "Meow!"
    
    def mengeong(self):
        print(f"{self.nama} mengeong: {self.suara()}")

class Burung(Hewan):
    def __init__(self, nama, spesies):
        super().__init__(nama)
        self.spesies = spesies

    def terbang(self):
        print(f"{self.nama} sedang terbang")

class BurungElang(Burung):
    def __init__(self, nama):
        super().__init__(nama, "Elang")

    def suara(self):
        return "kleeearrr"
    
    def bicara(self):
        print(f"{self.nama} berkata: {self.suara()}")


anjing = Anjing("Chole", "Siberian Husky")
anjing.gonggong()
anjing.menyusui()

kucing = Kucing("Neo", "British Shorthair")
kucing.mengeong()
kucing.menyusui()

elang = BurungElang("aigle")
elang.bicara()
elang.terbang()