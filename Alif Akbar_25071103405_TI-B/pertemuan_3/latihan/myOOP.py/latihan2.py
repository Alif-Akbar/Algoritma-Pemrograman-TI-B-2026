#POLYMORPHISM

class Notifikasi:
    def __init__(self, message):
        self.message = message

    def kirim(self):
        return self.message

class Email(Notifikasi):
    def __init__(self, message):
        super().__init__(message)

    def kirim(self):
        return super().kirim()
        return "Mengirim notifikasi melalui Email"

class SMS(Notifikasi):
    def __init__(self, message):
        super().__init__(message)

    def kirim(self):
        return super().kirim()
        return "Mengirim notifikasi melalui SMS"

a = Email(input("Masukkan pesan email: "))
b = SMS(input("Masukkan pesan SMS: "))

print(a.kirim())
print(b.kirim())