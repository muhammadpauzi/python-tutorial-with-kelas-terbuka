# Private property adalah property yang hanya ..
# .. dapat diakses dari dalam kelas itu saja

# Untuk menentukan property itu private adalah ..
# .. dengan meletakan __ di awal nama propertynya

class User():
    # __name
    def __init__(self, name):
        # Property private
        self.__name = name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName
        return self.getName()


User1 = User("Pauzi")

print(User1.getName())
print(User1.setName("Pauzi Saja"))
