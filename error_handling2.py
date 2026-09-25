while True:

    try:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Program dihentikan.")
            break

        user_input = int(user_input)

        if user_input in [1, 2, 3, 4, 5, 6, 7]:
            print(f"Kamu menginput {user_input}")
        else:
            print("Silahkan input angka 1 sampai 7.")

    except ValueError:
        print("Input harus berupa angka 1 sampai 7!")

    finally:
        print("--- proses selesai ---\n")