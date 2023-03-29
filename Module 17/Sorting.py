class DataBase:
    def __init__(self, name, age, job):
        self.name = name
        self._age = age
        self.job = job

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def __repr__(self):
        return f"{self.age}"


P1 = DataBase("Ivanov Ivan", 22, "doctor")
P2 = DataBase("Petrov Petr", 55, "driver")
P3 = DataBase("Third Person", 42, "unemployed")

list_of_people = [P1, P2, P3]
list_of_people.sort(key=lambda x: x.age)
print (list_of_people)
