# belajar csv reader
import csv

with open('produk.csv', 'r') as file:
    data = csv.reader(file)

    for row in data:
        print(row)