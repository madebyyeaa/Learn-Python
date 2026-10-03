import csv

data = [
    ['kode', 'nama', 'harga', 'stok'],
    ['P001', 'Indomie', 3000, 15],
    ['P002', 'Aqua', 4000, 15],
    ['P003', 'Teh Botol', 5000, 10],
    ['P004', 'Roti', 7000, 8]
]

with open('latihan_produk_baru.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(data)