import requests
from datetime import datetime

kota = input("Masukkan Nama Kota: ")

# Mendapatkan latitude dan longitude dari kota
url = f"https://nominatim.openstreetmap.org/search?city={kota}&format=json"
response = requests.get(url).json()

# Memeriksa apakah kota ditemukan
if not response:
    print(f"Kota '{kota}' tidak ditemukan.")
else:
    lat = response[0]["lat"]
    lon = response[0]["lon"]

    # Mendapatkan jadwal sholat menggunakan latitude dan longitude
    url = f"http://api.aladhan.com/v1/timings?latitude={lat}&longitude={lon}&method=2"
    response = requests.get(url).json()

    timings = response["data"]["timings"]

    # Mengubah waktu ke format 12 jam
    for key in timings:
        timings[key] = datetime.strptime(timings[key], "%H:%M").strftime("%I:%M %p")

    today = datetime.today().strftime("%A, %B %d, %Y")
    print(f"\nJadwal waktu sholat untuk {kota} ({lat}, {lon}) pada {today}:\n")

    print(f"Imsak: {timings['Imsak']}")
    print(f"Subuh: {timings['Fajr']}")
    print(f"Dhuhr: {timings['Dhuhr']}")
    print(f"Ashar: {timings['Asr']}")
    print(f"Maghrib: {timings['Maghrib']}")
    print(f"Isya: {timings['Isha']}")
