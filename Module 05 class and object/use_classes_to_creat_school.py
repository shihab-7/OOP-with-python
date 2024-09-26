class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str:
        return f'Student with name : {self.name}, class : {self.current_class}, id : {self.id}'
""" eitake bola hoy representation functrion
 eita use na korle class type compiler a show korbe
 """

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher : {self.name} , subject : {self.subject}'


class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name , subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id : {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('welcode to ', self.name)
        print('----------OUR Teachers-----------')
        for teacher in self.teachers:
            print(teacher)
        print('----------OUR Studentss-----------')
        for student in self.students:
            print(student)
        return "All Done for now"
    

alia = Student('Alia hasan', 9 , 1)
print(alia) # eita print hoito na

ranbir = Teacher('Ranbir', 'English',101)
print(ranbir)

phitron = School('phitron')
phitron.enroll('alia',5200)
phitron.enroll('sonia',8000)
phitron.enroll('saiba',6500)
phitron.enroll('samia',10000)

phitron.add_teacher('Tom Cruise', 'DS')
phitron.add_teacher('Dora', 'algo')
phitron.add_teacher('Subeen', 'data base')

print(phitron)