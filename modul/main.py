# Mengambil seluruh module
import matematika;

hasil = matematika.tambah(10, 5)

print(hasil)

# Mengambil beberapa fungsi
from matematika import tambah, kurang

print(tambah(10, 5))
print(kurang(10, 5))