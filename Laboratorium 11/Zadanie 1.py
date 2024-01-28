import json

from numpy import average


class Student:
    def __init__(self, name, email, grades, is_adult):
        self.name = name
        self.email = email
        self.grades = grades
        self.is_adult = is_adult

    def to_json(self):
        return json.dumps(self.__dict__, indent=2)

def avg(student):
    if len(student.grades) > 0:
        return average(student.grades)
    else:
        return 0.

def load_students():
    with open('students.json', 'r') as file:
        data = json.load(file)
    students = []
    for s in data['students']:
        student = Student(s['name'], s['email'], s['grades'], s['is_adult'])
        students.append(student)
    return students

def add_average(students):
    for student in students:
        student.average = avg(student)

def save_students(path, students):
    with open(path, 'w') as file:
        json.dump([student.__dict__ for student in students], file, indent=2)

if __name__ == "__main__":
    students = load_students()
    add_average(students)
    save_students('students_average.json', students)




