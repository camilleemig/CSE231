###########################################################
    #  Computer Project #11
    #
    #    Imports classes
    #    Tests making a grade
    #    Tests making a students
    #    Tests adding a grade
    #    Tests calculating final grade
    #    Makes two students with different final scores
    #    Compares students (>,<, =)
    #
    ###########################################################

import classes

print("Testing making a grade")
new_grade = classes.Grade('test', 100, .5) #test __init__()
print(new_grade, '\n') #test __str__()

print("Testing making a grade with incorrect parameters")
new_grade_two = classes.Grade(11,'a', 'b') #test __init__()
print(new_grade_two, '\n') #test __str__()

print("Testing making a Student with correct parameters- Grace")
grace_grade_one = classes.Grade('test', 100, .5) #test __init__()
grace_grade_two = classes.Grade('test2', 50, .5) #test __init__()
Grace = classes.Student(1,"Grace","A",[grace_grade_one,grace_grade_two]) #test __init__()
print(Grace) #test __str__()

print("Testing making a Student with incorrect parameters- No Name") #test __init__()
NoName = classes.Student('1',2,3,[4,5])
print(NoName) #test __str__()


print("Testing adding a grade- Julie")
Julie = classes.Student(1, "Julie", "a")
print(Julie)
julie_grade_one = classes.Grade('test', 100, .5) #test __init__()
Julie.add_grade(julie_grade_one)
print(Julie)
print("Testing adding a grade- Julie")
julie_grade_two = classes.Grade('test2', 50, .5) #test __init__()
Julie.add_grade(julie_grade_two)
print(Julie) #test __str__()


print("Testing calculating final grade- Julie")
print(Julie.calculate_grade(), '\n') #test calculate_grade()

print("Testing a high scoring Student- Kayla")
kayla_grade_one = classes.Grade('test', 100, 1) #test __init__()
Kayla = classes.Student(1,"Kayla","A",[kayla_grade_one]) #test __init__()
print(Kayla) #test __str__()

print("Testing a low scoring student- Sam")
sam_grade_one = classes.Grade('test', 0, 1) #test __init__()
Sam = classes.Student(1,"Sam","A",[sam_grade_one]) #test __init__()
print(Sam) #test __str__()

print("Testing Kayla < Sam")
print(Kayla < Sam) #test __lt__()
print("Testing Sam < Kayla")
print(Sam < Kayla) #test __lt__()
print("Testing Kayla > Sam")
print(Kayla > Sam) #test __gt__()
print("Testing Sam > Kayla")
print(Sam > Kayla) #test __gt__()
print("Testing Sam > string 'a'")
print(Sam > 'a') #test __gt__() with incorrect parameters
print("Testing Sam > int 0")
print(Sam > 0) #test __gt__() with incorrect parameters
print()

print("Testing two equal storing students- Macey and Jess")
macey_grade_one = classes.Grade('test', 88, 1) #test __init__()
Macey = classes.Student(1,"Macey","A",[macey_grade_one]) #test __init__()
print(Macey) #test __str__()
jess_grade_one = classes.Grade('test', 88, 1) #test __init__()
Jess = classes.Student(1,"Jess","A",[jess_grade_one]) #test __init__()
print(Jess) #test __str__()

print("Testing Macey == Jess")
print(Macey == Jess) #test __eq__()
