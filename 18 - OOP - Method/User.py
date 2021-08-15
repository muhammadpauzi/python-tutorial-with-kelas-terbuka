class User():
    name = "Muhammad Pauzi"

    # Ini adalah method, dan argument self wajib ditulis
    def getName(self):
        # Self untuk mengakses property atau method yang ada ..
        # .. di dalam class ini dari setiap object
        # Mungkin seperti this di php & javascript
        return self.name

    def setName(self, newName):
        self.name = newName
        return self.getName()


User1 = User()

print(User1.getName())
print(User1.setName("Pauzi Saja"))
