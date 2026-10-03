import csv

with open('latihan_produk_baru.csv', 'w', newline= '') as file:
    fieldnames = ['kode', 'nama', 'harga', 'stok']

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # menulis ulang satu baris
    writer.writerow(
        {
            'kode' : 'P005',
            'nama' : 'Gas',
            'harga' : 25000,
            'stok' : 50,
        }
    )

    # menulis ulang dengan banyak baris
    writer.writerows(
        {
            'kode' : 'P005',
            'nama' : 'Gas',
            'harga' : 25000,
            'stok' : 50,
        },
        {
            'kode' : 'P006',
            'nama' : 'Galon',
            'harga' : 20000,
            'stok' : 100,
        }
    )