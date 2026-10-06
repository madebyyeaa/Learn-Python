import json

produk = {
    "kode" : "P007",
    "nama" : "Tisu Basah",
    "harga" : "15000",
    "stok" : "100",
}

hasil = json.dumps(produk)

print(produk)
print(type(produk))
print(type(hasil))