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