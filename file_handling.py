# Membuka file 
file = open('data.txt', 'r')
print(file.read())
file.close()

# Menulis ulang file
file = open('data.txt', 'w')
file.write('Halo yuk belajar file handling')
file.close()

# Menambahkan data diakhir file a / append 
file = open('data.txt', 'a')
file.write('\nBelajar dengan python nih')
file.close()

# Dengan with open file handling akan lebih bagus karena ketika blok code dijalankan otomatis akan terclose.
with open('data.txt', 'r') as file:
    print(file.read())

# Membaca file perbaris
with open('data.txt', 'r') as file:
    for data in file:
        print(data.strip())

# function read() digunakan untuk membaca semua isi file
with open('data.txt', 'r') as file:
    data = file.read()

print(data)

# function readline() digunakan untuk membaca satu baru pada isi file
with open('data.txt', 'r') as file:
    print(file.readline())
    print(file.readline())

# function readlines() digunakan untuk membaca seluruh baris dengan menghasilkan list
with open('data.txt', 'r') as file:
    data = file.readlines()
print(data)


