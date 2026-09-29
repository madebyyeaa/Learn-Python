import csv #modul default dari python 

# Membaca file CSV
with open('karyawan.csv', 'r') as file :
    data = csv.reader(file)

    for row in data:
        print(row)

# Mengakses kolom tertentu
with open('karyawan.csv', 'r') as file:
    data = csv.reader(file)

    for row in data:
        print(f'Nama: {row[0]}')
        print(f'Jabatan: {row[1]}')
        print(f'Gaji: {row[2]}')
        print('---')

# CSV dictionary
with open("karyawan.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        print(row["nama"])
        print(row["jabatan"])
        print(row["gaji"])

# Membuat CSV dengan python
data = [
    ["nama", "jabatan", "gaji"],
    ["Yoram", "IT Support", 3500000],
    ["Andi", "Admin", 3200000],
    ["Budi", "Supervisor", 5000000]
]

with open("karyawan_baru.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(data)

# Menambahkan data dengan csv

with open("karyawan.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Citra", "Kasir", 3000000])