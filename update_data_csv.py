import csv

produk = []

with open('latihan_produk_baru.csv', 'r', newline='') as file:
    data = csv.DictReader(file)

    for row in data:
        produk.append(row)

print(produk)

# update data
for row in produk:
    if row['kode'] == 'P001':
        row['stok'] = '40'

# tulis ulang update data

with open('latihan_produk_baru.csv', 'w', newline='') as file:
    fieldnames = ['kode', 'nama', 'harga', 'stok']

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(produk)

print('Data berhasil diupdate!')