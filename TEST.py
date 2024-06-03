import random

# Daftar kata-kata yang bisa ditebak
kata_kunci = ["apel", "jeruk", "pisang", "mangga", "stroberi", "semangka"]

# Memilih kata secara acak dari daftar
kata_terpilih = random.choice(kata_kunci)

# Membuat variabel untuk menyimpan jawaban pemain
tebakan = ""

# Maksimal jumlah kesempatan
maksimal_kesempatan = 3
kesempatan = 0

# Memulai permainan
print("Selamat datang di permainan Tebak Kata!")

while kesempatan < maksimal_kesempatan:
    # Menampilkan jumlah kesempatan yang tersisa
    sisa_kesempatan = maksimal_kesempatan - kesempatan
    print(f"Anda memiliki {sisa_kesempatan} kesempatan.")

    # Meminta pemain untuk menebak kata
    tebakan = input("Tebak kata: ").lower()

    # Memeriksa apakah tebakan benar
    if tebakan == kata_terpilih:
        print("Selamat, Anda benar!")
        break
    else:
        print("Tebakan Anda salah. Coba lagi.\n")
        kesempatan += 1

# Jika pemain kehabisan kesempatan
if kesempatan == maksimal_kesempatan:
    print(f"Anda kehabisan kesempatan. Kata yang benar adalah '{kata_terpilih}'.")

print("Terima kasih telah bermain!")
