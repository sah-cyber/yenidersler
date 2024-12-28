

class Person:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    salari_artim = lambda self, faiz: self.salary *(1+faiz/100)


person1 = Person('Leyla',2000)

new_salary = person1.salari_artim(10)

print(f"iwcinin adi {person1.name} mawwi: {person1.salary} artimli maawi {new_salary}:.2f")
