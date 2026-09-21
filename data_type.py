text = 'uang';                                          # String     (data yang hanya berupa text)
number = 7;                                             # Integer    (data yang hanya berupa angka)
decimal = 2.3;                                          # Float      (data yang berupa desimal)
person = True;                                          # Boolean    (data yang hanya memiliki nilai true atau false)
coordinates = (2.3, 1.4, 1.3);                          # Tuple
tools = ['laptop','keyboard','mouse','monitor','cpu'];  # List       (data yang berisi kumpulan informasi data)
unique = {1,2,3,3,4,5,6,7};                             # Set        (data tidak bisa duplicate)
users = {'Nama' : 'Yoram', 'Belajar' : 'Python'};       # Dictionary (databerisi key dan value)

# Cara mengecek tipe data yang digunakan di python print(type());

print(type(text));
print(type(number));
print(type(decimal));
print(type(person));
print(type(coordinates));
print(type(tools));
print(type(unique));
print(type(users));

# Latihan tipe data

first_name: str = 'Yoram';
last_name: str = 'Arijaya';
age: int = 28;

# Concatenation cara menggabungkan dua atau lebih data.
print('Nama depan ' + first_name + ' dan nama belakang saya ' + last_name + ' umur saya', str(age));

# f'' string = format, digunakan untuk membuat penulisan informasi data menjadi kelihatan rapi jika dibandingkan dengan cara concatenation.
print(f'Nama depan saya {first_name} dan nama belakang saya {last_name}, umur saya {str(age)}');