import json

class Person():
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст!")

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender in 'mMWw-':
            self.__gender = gender
        else:
            print("Недопустимый пол!")

    def peson_to_json (self):
        return {
            "Class_Person":{
            "Name: ": self.name,
            "Age: ": self.age,
            "Gender: ": self.gender
            }
        }

    def __str__(self):
        return (f"Имя: {self.__name}\nВозраст: {self.__age}\nПол: {self.__gender}")

class Student(Person):

    def __init__(self, name, age, gender, group, course):
        super().__init__(name, age, gender)
        self.group = group
        self.course = course

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
            self.__group = group

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        if 0 < course < 7:
            self.__course = course
        else:
            print("Недопустимый номер группы!")

    def student_to_json(self):
        return {
            "Class_Student": {
                "Name: ": self.name,
                "Age: ": self.age,
                "Gender: ": self.gender,
                "Group: ": self.group,
                "Course: ": self.course
            }
        }

    def __str__(self):
        return ( super().__str__() + (f"\nГруппа: {self.__group} \nКурс: {self.__course}"))

p = Person("Person", 22, 'm')
data_person = p.peson_to_json()
with open('my.json','w') as file:
    json.dump(data_person, file, indent=3)
with open('my.json','r') as file:
    data_person_load = json.load(file)
print(data_person_load)

s = Student("Student", 18, 'w',"ICT",2)
data_student = s.student_to_json()
with open('my.json','w') as file:
    json.dump(data_student, file, indent=3)
with open('my.json','r') as file:
    data_student_load = json.load(file)
print(data_student_load)

