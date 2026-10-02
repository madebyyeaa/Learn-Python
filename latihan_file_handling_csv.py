import csv

with open('produk.csv', 'r') as file:
    data = csv.DictReader(file)

    

    for row in data:
        harga = int(row["harga"])
        stock = int(row["stok"])

        total = harga * stock
        print(f'\n===== DATA PRODUK =====\n')
        print(f'Kode  : {row["kode"]}')
        print(f'Nama  : {row["nama"]}')
        print(f'Harga : Rp.{row["harga"]},-')
        print(f'Stock : {row["stok"]}\n')
        print(f'Total : {total}') # Menghitung total harga dari stok barang
        print('-----------------------')


