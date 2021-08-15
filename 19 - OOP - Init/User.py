# Init adalah constructor yang ada dipython
# Init otomtis berjalan pada saat class dinstansiasi pertama kali

class User():
    # Init __init__
    # Property name akan otomatis terbuat jika ditentukanself.name di init
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName
        return self.getName()


User1 = User("Pauzi")

print(User1.getName())
print(User1.setName("Pauzi Saja"))
