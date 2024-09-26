from School import School , ClassRoom , Subject
from persons import Student , Teacher


def main():
    school = School('Adam jee', 'UTTARA', )    

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # adding students
    abul = Student('Abul khan', eight)
    school.student_admission(abul)
    babul = Student('Babul khan', eight)
    school.student_admission(babul)
    sobul = Student('Sobul khan', eight)
    school.student_admission(sobul)

    #adding subjects
    physics_teacher = Teacher('Shahjahan Tapan Rana')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemestry_teacher = Teacher('Hazari Nag')
    chemestry = Subject('Chemestry', chemestry_teacher)
    eight.add_subject(chemestry)

    biology_teacher = Teacher('Azmal Gazi')
    biology = Subject('Biology', biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()

    print(school)

if __name__ == '__main__':
    main()