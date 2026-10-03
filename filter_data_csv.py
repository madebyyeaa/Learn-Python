import csv

# filter berdasarkan stok
with open('latihan_produk_baru.csv', 'r') as file:
    data = csv.DictReader(file)

    for row in data:
        stok = int(row['stok'])

        if stok < 100:
            print(f'Kode : {row['kode']}')
            print(f'nama : {row['nama']}')
            print(f'stok : {stok}')
            print('-----------------')

# filer berdasarkan nama
with open('latihan_produk_baru.csv', 'r') as file:
    data = csv.DictReader(file)

    for row in data:
        if row['nama'] == 'Indomie':
            print(row)

# filter berdasarkan harga
with open('latihan_produk_baru.csv', 'r') as file:
    data = csv.DictReader(file)

    for row in data:
        harga = int(row['harga'])

        if harga > 2500:
            print(f'{row['nama']} - Rp{harga}')

# filter berdasarkan input

batas_stok = int(input('Masukan stok maksimal: '))

with open('latihan_produk_baru.csv', 'r') as file:
    data = csv.DictReader(file)

    for row in data:
        stok = int(row['stok'])

        if stok <= batas_stok:
            print(f'Kode : {row['kode']}')
            print(f'nama : {row['nama']}')
            print(f'stok : {stok}')
            print('-----------------')