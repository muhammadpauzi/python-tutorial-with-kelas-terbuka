# Inheritance adalah pewarisan
#  Inheritace adalah mewarisi property atau method dari kelas yang diinheritance

class User():
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName
        return self.getName()


# Admin(User) adalah class class User akan mewarisi semua property atau method yang public ke class Admin
class Admin(User):

    def setStatus(self, newStatus):
        # Untuk mengakses method dari class parentnya adalah dengan mengunakan self
        return "User yang bernama \"" + self.getName() + "\" \nberstatus sebagai " + newStatus


# Class admin akan menggunakan __init__ dari class User
User1 = Admin("Pauzi", "Admin")

# Object dari Admin bisa mengunakan method dari class User yaotu getName() dan setName()
print(User1.getName())
print(User1.setName("Pauzi Saja"))
print(User1.setStatus("Member"))
