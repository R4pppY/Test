class penjual():
    def __init__(self, nama, barang, harga):
        self.nama = nama
        self.barang = barang
        self.harga = harga

        def jual(self, pembeli):
            print(f"{self.nama} menjual {self.barang} kepada {pembeli} dengan harga {self.harga}")
class pembeli():
    def __init__(self, nama):
        self.nama = nama

def mainProgram():
    print("Hubungan Antar penjual dan pembeli")
    Rafi = penjual("Rafi","Keyboard", 300.000)
    Ray = pembeli("Ray")
    Rafi.jual(Ray)
mainProgram()


        
 

        