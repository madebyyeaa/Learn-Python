# Membuka file 
file = open('readme.txt', 'r')
print(file.read())
file.close()

# Menulis ulang file
file = open('readme.txt', 'w')
file.write('Halo yuk belajar file handling')
file.close()

# Menambahkan data diakhir file a / append 
file = open('readme.txt', 'a')
file.write('\nBelajar dengan python nih')
file.close()

# 
with open('readme.txt', 'r') as file:
    print(file.read())

#
with open('readme.txt', 'r') as file:
    for data in file:
        print(data.strip())

