from pickle import dump, load


class Person:
    def __init__(self, age=None, first_name="John", second_name="Doe"):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def get_name(self):
        return f"{self.first_name} {self.second_name} of age {self.age}"

class Employee(Person):
    def __init__(self, salary : float, job : str, *args, **kwargs):
        ''' age,  first_name, second_name are optional parametres'''

        Person.__init__(self, *args, **kwargs)
        self.salary = salary
        self.job = job

    def __str__(self):
        return f"{self.job}, {self.get_name()}"

    def change_salary(self, new_salary):
        self.salary = new_salary

    def get_salary(self):
        return self.salary

    def __del__(self):
        print(str(self) + " is FIRED!!!")

'''

    Модуль pickle хорош тем, что прост в использовании и можно "из коробки"
    упаковывать/считывать любые обьекты используя обычные бинарыне файлы,
    но существует несколько недостатков : 
     - отсутствие сжатия (можно использовать модуль compressed_pickle)
     - НЕБЕЗОПАСНО считывать из непроверенных файлов, устройство pickle такое,
    что может выполниться нежелательный код

'''

mary = Employee(20000, "Cleaner", first_name="Mary", second_name="Jane", age=27)
print(mary)
print(f"Mary's salary : {mary.get_salary()}")

print("Saving Mary's info to file...")
with open("Mary", "wb") as save_file:
    dump(mary, save_file)

print("Deleting Mary info obj...")
del mary

print("Loading Mary's info...")
with open("Mary", "rb") as load_file:
    mary = load(load_file)

print(f"Loaded object : {mary}")