import csv

kode: str = input('Kode : ')
nama: str = input('Nama: ')
harga: int = input('Harga: ')
stok: int = input('stok: ')

with open('latihan_produk_baru.csv', 'a', newline= '') as file:
    fieldnames = ['kode', 'nama', 'harga', 'stok']

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writerow({
        'kode' : kode,
        'nama' : nama,
        'harga' : harga,
        'stok' : stok
    })

    print(f'Produk berhasil ditambahkan!')

    