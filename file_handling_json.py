import json

with open('produk.json', 'r') as file:
    data = json.load(file)

print(data)