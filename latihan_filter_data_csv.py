import csv

with open('latihan_produk_baru.csv', 'r') as file:
    data = csv.DictReader(file)

    for row in data:
        harga = int(row['harga'])
        stok = int(row['stok'])
        nilai_stok =  harga * stok 

        if nilai_stok >= 50000:
            print(f'Kode: {row['kode']}')
            print(f'Nama: {row['nama']}')
            print(f'Harga: {nilai_stok}')
            print('-------------------')
