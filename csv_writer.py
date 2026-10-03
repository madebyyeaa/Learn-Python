import csv

data = [
    ['kode', 'nama', 'harga', 'stok'],
    ['P001', 'Indomie', 3500, 20],
    ['P002', 'Aqua', 4000, 15],
    ['P003', 'Teh Botol', 5000, 10],
]
with open('produk_baru.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(data) # mencetak hanya satu baris
    writer.writerows(data) # mencetak banyak baris