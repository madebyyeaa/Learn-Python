import csv

while True :
    try :
        print(f'===== DATA PRODUK =====')

        with open('produk.csv', 'r') as file:
            data = csv.DictReader(file)

            for row in data:
                print(row["kode"])
                print(row["nama"])
                print(row["harga"])
                print(row["stok"])


    except :
        print(f'Jalankan ulang program')