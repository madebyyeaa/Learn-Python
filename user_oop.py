class User:
    def __init__(self, nama, dept):
        self.nama = nama
        self.dept = dept

    def tampilkan_data(self):
        print('Nama :', self.nama)
        print('Departemen :', self.dept)

user1 = User('Yoram', 'IT')

user1.tampilkan_data()