###########################################################
    #  Computer Project #11
    #
    #    Creates class Grade
    #        initialize function
    #        string representation functions
    #    Creates class Student
    #        initialize function
    #        string representation functions
    #        greater than, less than, equal to, functions
    #        add grade function
    #        calculate grade function
    ###########################################################

class Grade(object):
    """Model details of an assignment"""

    def __init__(self, assignment_name, assignment_grade, assignment_weight):
        """ Initialize assignment with name, grade, and weight """

        #Checks to make sure assignment name is a string
        if type(assignment_name) != str:
            print("Assignment name must be a string, it was", assignment_name)
            print("Assignment name is assigned to 'No Name'\n")
            assignment_name = 'No Name'

        #Checks to make sure the assignment grade is an integer or float
        if not isinstance(assignment_grade, (int, float)):
            print("Assignment grade must be an int or float, it was", assignment_grade)
            print("Assignment grade is assigned to 0\n")
            assignment_grade = 0.0

        #Checks to make sure the assignment weight is an integer or float
        if not isinstance(assignment_weight, (int,float)):
            print("Assignment weight must be an int or float, it was", assignment_weight)
            print("Assignment weight is assigned to 0\n")
            assignment_weight = 0.0

        #Assigns all object variables
        self.assignment_name = assignment_name
        self.assignment_grade = assignment_grade
        self.assignment_weight = assignment_weight

    def __str__(self):
        """ Returns a representation of aspects of grade as a string """
        string_representation =  "{:12}:{:>5.0f}%{:>7.2f}".format(\
        self.assignment_name, self.assignment_grade,self.assignment_weight)
        return string_representation

    def __repr__(self):
        """ Returns a representation of aspects of grade as a string """
        return self.__str__()

class Student(object):
    """Model aspects of a student"""

    def __init__(self, stu_id, first_name = "First", last_name = "Last", grade_list = None):
        """ Initialize student with an id, first name, last name, and grades"""
        #Checks to make sure that the student id is an integer
        if type(stu_id) != int:
            try:
                #tries to convert student id to an integer
                stu_id = int(stu_id)
                print("Converted student id to an integer")

            except ValueError:
                #Sets id to 0 if it could not convert to an int
                stu_id = 0
                print("Student id must be an integer, set to 0")
        #Checks to make sure that the name is a string
        if type(first_name) != str:
            print("First name must be a string, set to 'First'")
            first_name = 'First'

        #Checks to make sure that the name is a string
        if type(last_name) != str:
            print("Last name must be a string, set to 'Last'")
            last_name = 'Last'

        #Loops through each grade in the list to make sure it is a grade object
        correct_grade_list = []
        if grade_list != None:
            for grade in grade_list:
                if isinstance(grade, Grade):
                    correct_grade_list.append(grade)
        #Sets the grade list to None if there were no grades
        if correct_grade_list == []:
            correct_grade_list = None

        #Sets object variables
        self.stu_id = stu_id
        self.first_name = first_name
        self.last_name = last_name
        self.grade_list = correct_grade_list

    def __str__(self):
        """ Returns a representation of aspects of student as a string """
        string_representation = ''
        #Adds the name to print
        string_representation += self.last_name + ', ' + self.first_name + '\n'
        #Makes sure that there are grades to iterate through
        if self.grade_list != None:
            #Adds each grade to string to print
            for grade in self.grade_list:
                string_representation += grade.__str__() + '\n'
            #Adds final grade to print
            string_representation +=  "{:12}:{:>5.0f}%{:>7}\n".format('Final Grade',\
            self.calculate_grade(),'')
        #Prints this if there are no grades to calculate
        else:
            string_representation += "No grades avaliable\n"
        return string_representation

    def __repr__(self):
        """ Returns a representation of aspects of student as a string"""
        return self.__str__()

    def __gt__(self, other):
        """
        Compares final grades of two Student Objects, returns True of False
        """
        #Checks to make sure other is a Student object and thus will have the
        #calculate grade method
        if isinstance(other, Student):
            return self.calculate_grade() > other.calculate_grade()
        #Returns False if they are not the same type
        else:
            return False

    def __lt__(self, other):
        """
        Compares final grades of two Student Objects, returns True of False
        """
        #Checks to make sure other is a Student object and thus will have the
        #calculate grade method
        if isinstance(other, Student):
            return self.calculate_grade() < other.calculate_grade()
        #Returns False if they are not the same type
        else:
            return False
    def __eq__(self, other):
        """
        Compares equality of final grades of two Student objects,
        returns True of False
        """
        #Checks to make sure that other is a Student object and will have grades
        if isinstance(other, Student):
            #Checks equality of floats, as floats are not always exactly the same
            difference = abs(self.calculate_grade() - other.calculate_grade())
            return difference < 10**-6
        else:
            return False

    def add_grade(self, new_grade):
        """ Adds a new grade to a student's grades """
        #Makes sure that the new grade is a Grade object
        if isinstance(new_grade, Grade):
            #Checks to see if there are already grades to append to
            if self.grade_list == None:
                self.grade_list = [new_grade]
            else:
                self.grade_list.append(new_grade)
        #Prints an error statement if it is not a Grade object
        else:
            print("Was not able to append the new grade, which was:", new_grade)

    def calculate_grade(self):
        """ Calculates the final grade of a student, returns the final grade"""
        final_grade = 0
        #Makes sure that there are grades to iterate through
        if self.grade_list != None:
            for grade in self.grade_list:
                final_grade += grade.assignment_grade*grade.assignment_weight
        return final_grade

def isinstance(exp, type_or_tuple):
    """ Checks to see if a variable is of a certain type. Returns True or False"""
    if type(type_or_tuple) == tuple:
        for tupletype in type_or_tuple:
            if type(exp) == tupletype:
                return True
        return False
    else:
       if type(exp) == type_or_tuple:
           return True
       else:
           return False
