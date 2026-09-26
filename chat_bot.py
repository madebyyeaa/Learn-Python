<<<<<<< HEAD
bot_name: str = 'Yoram';
print(f'Halo saya {bot_name}! apa yang dapat saya bantu?');

while True:
    user_input: str = input('Yoram: ').lower();

    if user_input in ['hai', 'halo']:
        print(f'{bot_name}: Hai teman, sampai jumpa!');
    elif user_input in ['bye', 'sampai jumpa']:
        print(f'{bot_name} Bye! besok ketemu lagi ya teman.');
    else:
        print(f'{bot_name} maaf saya tidak mengerti ketik hai, halo, bye, sampa jumpa');
=======
user_bot: str = 'Bang IT'
print(f'{user_bot} : Woi sopan sikit abang IT ni, kendala apa?')

while True:
    user_input: str = input('You: ').lower()
    
    if user_input in ['help bang']:
        print(f'{user_bot}: Ada kendala apa?')
    elif user_input in ['mohon dibantu bang']:
        print(f'{user_bot}: Ada kendala apa cuk?!!')
    elif user_input in ['tdk ada jaringan bang', 'jaringan hilang']:
        print(f'{user_bot}: Oke down ya, restart dulu modemnya 15 menit')
    elif user_input in ['jaringan hilang']:
        print(f'{user_bot}: Sudah restart modem belum? restart dulu kalau belum!')
    else:
        print(f'Masukan kata kunci dengan sesuai panduan di atas coba lagi')
>>>>>>> 2d313e7 (belajar membuat dan mengimport modul)
