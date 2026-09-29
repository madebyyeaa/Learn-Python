# Latihan file handling membuat program penambahan data karyawan sederhana
while True:
    try:
        print("\n===== DATA KARYAWAN =====")
        menus: list[str] = [
            "1. Tambah data",
            "2. Lihat data",
            "3. Buat file baru",
            "4. Keluar"
        ]

        for menu in menus:
            print(menu)

        user_input: str = input("Pilih: ")

        if user_input == "1":
              nama = input('Nama: ')
              if nama == 'exit':
                  break
              
              with open('karyawan.txt', 'a') as file:
                data = file.write(nama + '\n')
                print("Data berhasil ditambahkan!")

        elif user_input == "2":
            with open('karyawan.txt', 'r') as file:
                data = file.read()
                print(data)

        elif user_input == "3":
            newFile = input('Nama file: ')
            try :
                with open(newFile, 'x') as file:
                    file.write(newFile)
                print(f'{newFile} was created!')
            except FileExistsError :
                print(f'Nama file sudah ada, buat dengan nama file lain')

        elif user_input == "4":
            print("Program dihentikan.")
            break

        else:
            raise ValueError

    except ValueError:
        print("Input harus berupa pilihan 1 sampai 4!")


