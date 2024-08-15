import statistics

# Data mahasiswa dan nilai
mahasiswa = [
    {"nama": "Alice", "kelas": "A"},
    {"nama": "Bob", "kelas": "A"},
    {"nama": "Charlie", "kelas": "B"},
    # ...
]

nilai = [
    {"mahasiswa": "Alice", "matkul": "Algoritma dan Struktur Data", "nilai": 85},
    {"mahasiswa": "Bob", "matkul": "Algoritma dan Struktur Data", "nilai": 90},
    {"mahasiswa": "Charlie", "matkul": "Algoritma dan Struktur Data", "nilai": 75},
    # ...
]

# Menghitung nilai tertinggi dan terendah
nilai_tertinggi = max(nilai, key=lambda x: x["nilai"])["nilai"]
nilai_terendah = min(nilai, key=lambda x: x["nilai"])["nilai"]

# Mencari rata-rata nilai
nilai_rata = statistics.mean([x["nilai"] for x in nilai])

# Mencari mahasiswa dengan nilai tertinggi dan terendah
mahasiswa_tertinggi = [x for x in nilai if x["nilai"] == nilai_tertinggi]
mahasiswa_terendah = [x for x in nilai if x["nilai"] == nilai_terendah]

# Menampilkan hasil
print("Nilai Tertinggi:", nilai_tertinggi)
print("Nilai Terendah:", nilai_terendah)