import csv

with open('latihan_produk_baru.csv', 'a', newline= '') as file:
    writer = csv.DictWriter(
        file,
        fieldnames= ['kode', 'nama', 'harga', 'stok']
    )

    writer.writerow({
        'kode' : 'P005',
        'nama' : 'Pensil',
        'harga' : 2500,
        'stok' : 100
    })