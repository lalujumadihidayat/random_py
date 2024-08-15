kasih_teks = input("Masukkan teks : ")
jumlah_teks = len(kasih_teks)
print("jumlah teks :", jumlah_teks)

def main():
    teks = input("Masukkan Karakter: ")
    jumlah = int(input("Berapa  : "))

    hasil = teks * jumlah
    print(f"oke nih :\n\n{hasil}\n")

    if __name__ == "__main__":
        main()