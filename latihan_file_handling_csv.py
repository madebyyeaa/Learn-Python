import csv

while True :
    try :
        createFile = input('Buat nama file: ')
        try:
            with open(createFile, 'x') as file:
                file.write(createFile)
            print(f'{createFile} berhasil dibuat')
        except FileExistsError :
                print(f'Nama file sudah ada, buat dengan nama file lain')
    except : # istirahat dulu ya mau tidur