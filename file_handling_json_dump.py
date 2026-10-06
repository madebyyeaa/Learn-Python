import json

produk = {
    "kode": "P001",
    "nama": "Indomie",
    "harga": "2500",
    "stok": "300",
}

with open('produk.json', 'w', newline='') as file:
    data = json.dump(produk, file, indent=4)

    print("Data berhasil disimpan")