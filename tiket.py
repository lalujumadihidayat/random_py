from datetime import datetime
current_datetime = datetime.now()
date_and_time = current_datetime.strftime("%Y-%m-%d -%H:%M:%S")
print("_"*55)

dewasa = 4000
anak = 2000

print("Harga tiket : Dewasa (>15 tahun)     = Rp", dewasa)
print("Harga tiket : Anak   (<15 tahun)     = Rp", anak)

print("_"*55)
jumlah_dewasa = int(input("Pesanan tiket untuk dewasa >17 tahun  : "))
jumlah_anak = int(input("Pesanan tiket untuk anak-anak <17 tahun  :  "))

harga_dewasa = jumlah_dewasa * dewasa
harga_anak = jumlah_anak * anak
total_harga = harga_dewasa + harga_anak

diskon = int(total_harga * 0.1)
if total_harga > 300000:
    harga_setelah_diskon = total_harga - diskon
else :
    harga_setelah_diskon = total_harga

print("_"*55)
print("- Tiket masuk ke kolam -")
print("-"*55)
print("\nPesanan tiket untuk dewasa  =", jumlah_dewasa, "orang")
print("Pesanan tiket untuk anak-anak  =",jumlah_anak, "orang")
print("\nHarga tiket dewasa      = Rp",harga_dewasa)
print("Harga tiket anak-anak    =Rp",harga_anak)
print("\nJUMLAH HARGA TIKET    = Rp", total_harga)
print("_"*55)

if total_harga >= 300000:
    print(f"\nAnda dapat diskon sebesar Rp {diskon}")
    print(f"Harga setelah diskon adalah Rp {harga_setelah_diskon}")
    print("_"*55)