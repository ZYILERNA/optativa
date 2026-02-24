class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
#cuando eliminamos pass del constructor, debemos pasar los parametros.

my_person = Person("Zhen", "Yang")
print(f"{my_person.name} {my_person.surname}")
print(my_person.name)
print(my_person.surname)

class person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

def walk(self):
    print(f"{self.full_name} está caminando")

#uso del objeto

my_other_person = person("Zhen", "Yang")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Zhen (El loco de los perros)"
print(my_other_person.full_name)
my_other_person.walk()