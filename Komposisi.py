class Warga():
    def __init__(self, nama):
        self.nama = nama
        self.ktp = KTP(None, None)
class KTP():
    def __init__(self, NIK, nomor):
        self.NIK = NIK
        self.nomor = nomor
    def cetak(self, warga):
        print(f"kepemilikan NIK KTP ini {self.NIK} adalah {warga.nama}")
def main():
    rafi = Warga("Rafi")
    rafi.ktp.NIK = input("silahkan masukkan NIK KTP: ")
    rafi.ktp.cetak(rafi)
main()
        
        