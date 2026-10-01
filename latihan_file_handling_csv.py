import csv

with open('produk.csv', 'r') as file:
    data = csv.DictReader(file)

    for row in data:
        print(f'\n===== DATA PRODUK =====\n')
        print(f'Kode  : {row["kode"]}')
        print(f'Nama  : {row["nama"]}')
        print(f'Harga : Rp.{row["harga"]},-')
        print(f'Stock : {row["stok"]}\n')
        print('-----------------------')