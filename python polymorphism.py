
class Person:
    def __init__(self, name, age, address):
        self._name = name  # underscore indicates a "protected" attribute
        self._age = age
        self._address = address

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_address(self):
        return self._address

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_address(self, address):
        self._address = address

person1 = Person("Talha ahmad", 21, "sargodha")

# Accessing attributes using getters
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Address:", person1.get_address())

# Modifying attributes using setters
person1.set_name("Talha diyar")
person1.set_age(22)
person1.set_address("Lahore")

# Accessing modified attributes
print("\nModified Attributes:")
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Address:", person1.get_address())

