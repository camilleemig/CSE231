###########################################################
    #  Computer Project #11
    #
    #    Imports classes
    #    Trys to open two files
    #    Reads assignment weights from file
    #    Reads assignment names from file
    #    Reads student grades and ids from file
    #    Seperates student grades and ids
    #    Associates student grades as Grade objects to student ids
    #    Makes a list of student objects
    #    Prints the student objects
    #    Calculates average and prints average
    #
    ###########################################################

import classes

try:
    #Trys to open files, stops program if error occurs
    grades = open('grades.txt','r')
    students = open('students.txt','r')

    #Gets weights from the first line, converts to floats
    weights = grades.readline().split()
    weights = weights[1:]
    for i,weight in enumerate(weights):
        weights[i] = float(weight)

    #Gets project names from the next line, gets rid of id column header
    project_names = grades.readline().split()
    project_names = project_names[1:]

    #Loops through remaining lines, appending a list of a student's grades
    #to a list of all of the student's grades
    students_grades = []
    for line in grades:
        students_grades.append(line.split())

    #Seperates student ids from the student's grades, maintaining order
    student_ids = []
    for student in students_grades:
        student_ids.append(int(student.pop(0)))

    #Makes a dictionary relating the student ids and the list of Grade objects
    grades_dictionary = {}
    for i in range(len(students_grades)):
        for j in range(len(students_grades[i])):
            students_grades[i][j] = classes.Grade(project_names[j],\
            float(students_grades[i][j]),weights[j])
        grades_dictionary[int(student_ids[i])] = students_grades[i]


    students_list = []
    for line in students:
        #Gets student information from students file
        information = line.split()
        stu_id = information[0]
        stu_first = information[1]
        stu_last = information[2]
        #makes a student object from information in the students file and
        #appends it to a list
        students_list.append(classes.Student(int(stu_id), stu_first, stu_last,\
        grades_dictionary[int(stu_id)]))

    #Sets variables for class average
    number_of_students = 0
    class_average = 0
    
    #Prints data for each student and adds each final grade to the class average
    for student in students_list:
        print(student)
        class_average += student.calculate_grade()
        number_of_students += 1

    #Computes and prints class average
    class_average = class_average/number_of_students
    print("{}{:.2f}%".format("The class average is: ", class_average))

except FileNotFoundError:
    print("Could not successfully open file")
