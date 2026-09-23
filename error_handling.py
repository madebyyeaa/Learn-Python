a, b = 23, 'eleven'

try:
    print(a + b)
except Exception as e:
    print(f'Something went wrong: {e}')
