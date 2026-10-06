import json

data = '{"kode" : "P002", "nama" : "Teh Botol", "harga" : "4500", "stok" : "100"}'

hasil = json.loads(data) #membaca file JSON dari string

print(hasil)
print(hasil['nama'])