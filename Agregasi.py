class Karyawan():
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def info(self, honor):
        totalGaji = honor.gajiPokok + honor.lembur + honor.tunjangan
        totalGaji -= honor.pajak
        print(f"{self.nama} mendapatkan honor sebanyak {totalGaji}")
class Honor():
    def __init__(self, gajiPokok, lembur, tunjangan, pajak):
        self.gajiPokok = gajiPokok
        self.lembur = lembur
        self.tunjangan = tunjangan
        self.pajak = pajak
def main():
        print(" Agregasi (saling memiliki)")
        Reiji = Karyawan("Reiji", 25)
        honor = honor(5000000, 3000000, 2000000, 1000000)
        Reiji.info(honor)
main()
        