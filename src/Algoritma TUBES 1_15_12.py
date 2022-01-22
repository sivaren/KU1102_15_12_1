# Nama/NIM  :   Rahmat Al Fajri - 16520171
#               Rava Naufal A   - 16520411
#               Ray Clement     - 16520371
#               Rio Alexander   - 16520181

# Program    : Simluasi_Lift
# Deskripsi  : Penggunaan lift dalam kehidupan sehari-hari

# KAMUS
# gerak_lift        : bool untuk menyimmpan arah gerak lift
# lantai            : arr untuk menyimpan semua lantai yg dituju penumpang
# lantai_naik       : arr untuk menyimpan lantai naik
# lantai_turun      : arr untuk menyimpan lantai turun
# lantai_tujuan     : arr untuk menyimpan lantai tujuan lift
# lantai_sekarang   : int untuk menyimpan lantai sekarang
#
# total_penumpang   : int untuk menumpang jumlah total penumpang
# lantai_penumpang  : arr sebagai tabel frekuensi lantai penumpang

# ALGORITMA

# Definisi prosedur untuk menjemput penumpang
def jemput_penumpang():
    global lantai_sekarang
    global gerak_lift

    j = int(input("Lantai Penumpang: "))

    for i in range(lantai_sekarang, j + 1):
        if i == j:
            print(f"----Lantai {i}-----")
            lantai_sekarang = j
            return
        else:
            print(f"{i} ↑")

    for i in range(lantai_sekarang, j - 1, -1):
        if i == j:
            print(f"----Lantai {i}----")
            lantai_sekarang = j
            return
        else:
            print(f"{i} ↓")


# Definisi fungsi untuk menentukan jumlah penumpang
def jumlah_penumpang():
    # KAMUS Lokal
    # n     : int untuk menyimmpan jumlah penumpang yang masuk
    # Asumsi berat tiap penumpang adalah 60 Kg
    # Asumsi kapasitas berat maksimum lift adalah 600 Kg

    # Algoritma
    while True:
        n = int(input("Masukkan jumlah penumpang : "))

        if n + total_penumpang > 10:
            print("Penumpang melebihi kapasitas")
        else:  # n <= 10
            return n + total_penumpang


# Definisi fungsi untuk menginput lantai tujuan penumpang
def input_lantai(n):
    # KAMUS Lokal
    # temp_penumpang    : arr untuk menyimpan semua lantai yg diinput penumpang
    # n                 : int untuk menyimpan jumlah penumpang yang masuk
    # Asumsi setiap penumpang hanya dapat menginput satu lantai tujuan
    # Asumsi inputan lantai yang dituju setiap penumpang pasti benar
    # Asumsi di suatu gedung yang hanya ada 10 lantai
    # Asumsi penumpang tidak menginput lantai tujuan yang sama dengan posisi sekarang lift berada

    # Algoritma

    global gerak_lift
    global total_penumpang

    lantai_temp = []

    for i in range(n):
        j = int(input(f"Masukkan lantai tujuan orang ke-{i + 1}: "))
        lantai_temp.append(j)
        if j == lantai_sekarang:
            lantai_penumpang[j - 1] -= 1
            total_penumpang -= 1
        lantai_penumpang[j - 1] += 1

    for i in lantai_temp:
        if not (i in lantai) and i != lantai_sekarang:
            if i > lantai_sekarang:
                lantai_naik.append(i)
            elif i < lantai_sekarang:
                lantai_turun.append(i)
            lantai.append(i)

    lantai.sort()

    if gerak_lift:  # True = naik
        return lantai_naik
    else:
        return lantai_turun


# Definisi prosedur bila sudah sampai ke lantai yang dituju
def sampai_lantai(n):
    # KAMUS Lokal:
    # n   : int untuk menyimpan lantai sekarang

    # Algoritma
    global total_penumpang
    global lantai_penumpang

    lantai.remove(n)
    lantai_tujuan.remove(n)
    total_penumpang -= lantai_penumpang[n - 1]
    lantai_penumpang[n - 1] = 0


# Definisi prosedur mengubah arah gerak lift
def balik_arah():
    # Algoritma
    global lantai_tujuan
    global gerak_lift
    global lantai_sekarang

    if gerak_lift:
        lantai_sekarang -= 1
        lantai_tujuan = lantai_turun
    else:
        lantai_sekarang += 1
        lantai_tujuan = lantai_naik

    gerak_lift = not gerak_lift


# Definisi prosedur untuk menginput kondisi awal lift
def input_awal():
    # Algoritma
    global total_penumpang
    global lantai_sekarang
    global lantai_tujuan
    global gerak_lift

    jemput_penumpang()
    print()
    total_penumpang = jumlah_penumpang()
    lantai_tujuan = input_lantai(total_penumpang)

    if lantai_tujuan == []:
        balik_arah()
    print()


# Main Program

print("---Selamat Datang---")

gerak_lift = True
lantai = []
lantai_naik = []
lantai_turun = []
lantai_sekarang = 1

total_penumpang = 0
lantai_penumpang = [0 for i in range(10)]  # Tabel frekuensi tujuan penumpang
temp_penumpang = 0

input_awal()

while True:
    # Lift mulai bergerak
    while total_penumpang!=0:

        if gerak_lift:
            # Jika lift bergerak ke atas
            if lantai_sekarang in lantai_tujuan:
                # Jika lantai sekarang adalah lantai yang dituju
                sampai_lantai(lantai_sekarang)

                # Output user
                print(f'----Lantai {lantai_sekarang} sisa {total_penumpang} orang----')
                total_penumpang -= lantai_penumpang[lantai_sekarang - 1]
                print(lantai)

                # Tambahan penumpang
                if input("Apakah ada tambahan orang? (Y/N) ").lower() == "y":
                    # Jika ada tambahan penumpang
                    temp_penumpang = total_penumpang
                    total_penumpang = jumlah_penumpang()
                    lantai_tujuan = input_lantai(total_penumpang - temp_penumpang)
                print()

            else:
                # Jika lantai sekarang bukan lantai yang dituju
                print(f"{lantai_sekarang} ↑")

            if lantai_tujuan == []:
                # Jika lantai tujuan sudah kosong (habis)
                balik_arah()
                break

            # Lantai bergerak naik
            lantai_sekarang += 1

        elif not gerak_lift:
            # Jika lantai bergerak ke bawah
            if lantai_sekarang in lantai_tujuan:
                # Jika lantai sekarang adalah lantai yang dituju
                sampai_lantai(lantai_sekarang)

                # Output user
                print(f'----Lantai {lantai_sekarang} sisa {total_penumpang} orang----')
                total_penumpang -= lantai_penumpang[lantai_sekarang - 1]
                print(lantai)

                # Tambahan penumpang
                if input("Apakah ada tambahan orang? (Y/N) ").lower() == "y":
                    # Jika ada tambahan penumpang
                    temp_penumpang = total_penumpang
                    total_penumpang = jumlah_penumpang()
                    lantai_tujuan = input_lantai(total_penumpang - temp_penumpang)
                print()

            else:
                # Jika lantai sekarang bukan lantai yang dituju
                print(f"{lantai_sekarang} ↓")

            if lantai_tujuan == []:
                # Jika lantai yang dituju sudah kosong (habis)
                balik_arah()
                break

            # Lantai bergerak turun
            lantai_sekarang -= 1

    # Ketika semua penumpang telah keluar
    if total_penumpang == 0:
        print("~Selamat Jalan~")

        if input("Mau Lagi? (Y/N) ").lower() == "y":
            # Jika ada penumpang baru yang masuk
            print()
            if gerak_lift:
                lantai_sekarang -= 1
            else:
                lantai_sekarang += 1

            input_awal()
        else:
            # Keluar Program
            break
