# function
def func() -> None :
    print(f'Hi, Yoram!')

func();

# membuat function dengan nama add
def add(a: float, b: float) -> float:
    print(f'Jumlah uang didompet saya: {a} + {b}')
    return a + b;

print(f'Total : Rp.{add(500000, 25000)},-');
print(f'Total : Rp.{add(525000, 4000000)},-');

# membuat function dengan nama greet
def greet(name: str, greeting: str = 'Hello') -> None:
    print(f'{greeting}, {name}!');

greet('Yoram', 'Halo');
greet('Yoram');