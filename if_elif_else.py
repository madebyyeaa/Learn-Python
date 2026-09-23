# if ... elif ... else digunakan untuk mengatur flow pada aplikasi

while True:
    user_input: str = input('You: ');

    if user_input == 'hello':
        print('Bot: hello!')
    elif user_input == 'how are you?':
        print('Bot: good, how are you?')
    else:
        print('Bot: Sorry, I did not understand that.')