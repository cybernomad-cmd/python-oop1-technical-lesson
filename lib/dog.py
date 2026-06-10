class Dog:
  def __init__(self, name, breed, age, last_checkup=None):
    self.name = name
    self.breed = breed
    self.age = age
    self.last_checkup = last_checkup
    
  def checkup(self, date):
    print(f"Checking up with {self.name} on {date}")
    self.last_checkup = date
    
  def birthday_celebration(self):
    self.age += 1
    print(f"{self.name} is turning {self.age}")
    
  def get_age(self):
    return self.age
  
def get_age(self):
    return self._age

def set_age(self, value):
    if type(value) is int and value >= 0:
        self._age = value
    else:
        print("Not valid age")

age = property(get_age, set_age)

fido = Dog("Fido", "Golden Retriever", 5, "06/10/2026")

zanzi = Dog(
  name="Zanzi",
  breed="Big Black Dog",
  age=3
)
  
print(fido.age)
fido.birthday_celebration()
print(fido.age)

print(zanzi.last_checkup)
zanzi.checkup("07/15/2026")
print(zanzi.last_checkup)


balto = Dog("Balto", "Husky", "Not an age")
steele = Dog("Steele", "Husky", -10)