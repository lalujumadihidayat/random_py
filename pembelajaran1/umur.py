import datetime as dt
print("Silahkan Masukkan Kapan Anda Lahir")
a = int(input("Tanggal:"))
b = int(input("Bulan:"))
c = int(input("Tahun:"))

x = dt.date(c,b,a)
print(f"Anda Lahir Pada : {x}")
print(f"Harinya Adalah : {x:%A}")

y = dt.date.today()
print(f"Tanggal Saat Ini : {y}")

date = y-x
tahun=date.days//365
bulan=(date.days % 365)//30
tanggal=(date.days % 365)

print(f"""Umur Anda Saat Ini :\t{tahun} tahun
\t\t\t{bulan} bulan
\t\t\t{tanggal} hari
""")