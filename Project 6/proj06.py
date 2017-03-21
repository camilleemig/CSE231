###########################################################
    #  Computer Project #6
    #
    #  Algorithm
    #   Call a function to prompt for a file name until one opens properly
    #   Call a function to read the wanted data into a list
    #   Call a function to count differences in victims and perpetrators
    #   Call a function to print the formatted data  
    ###########################################################
#1: yes, more minorities are excuted than whites, as shown by 273 minorities
#   executed and 225 whites executed
#2: yes, more minorites are executed for killing white than whites executed
#   for killing minorities, (28 minority on white, 7 white on minority)
#3: yes, because there were 65 executions where a man killed a woman, 
#   and 0 executions where a woman killed a man
#4: yes, 118 men were killed, while only 1 woman was killed

import csv

def open_file():
    """
        Prompts for a file name until one opens properly
        Returns:  The object of the open file
        """
    while True:
        try:
            file_name = input("Enter a file name: ")
            fp = open(file_name, 'r')
            break
        except FileNotFoundError:
            print("Error. Please try again")
    return fp

def read_file():
    """
        Calls open_file and converts data to a list
        Returns:  A list of formatted data from the file
        """
    file = open_file()
    csv_fp = csv.reader(file)
    usable_data = []
    #Gets the wanted data from columns 15, 16, and 27
    for L in csv_fp:
        converter = L[15], L[16], L[27] 
        usable_data.append(tuple(converter))
    return usable_data
    
def print_data(white_count, black_count, hispanic_count, minority_count,\
    male_count, female_count, minority_on_white_count, white_on_minority_count\
    , male_on_female_count, female_on_male_count, total_count):
    """
        Prints formatted data
        Count Variables: Counts of each different item to print        
        Returns:  None
        """
    print("="*30)
    print("White vs Minority")
    print("N = {}".format(white_count + black_count + hispanic_count))    
    print("White: {}".format(white_count))
    print("Black: {}".format(black_count))
    print("Hispanic: {}".format(hispanic_count))
    print("Minority = Black + Hispanic: {}".format(minority_count)) 
    print("="*30)
    print("Male vs Female")
    print("N = {}".format(int(male_count) + int(female_count)))
    print("Male: {}".format(male_count))
    print("Female: {}".format(female_count))
    print("="*30)
    print("Difference between perpetrator and victim")   
    print("N = {}".format(total_count))
    print("Minority on white: {}".format(minority_on_white_count))
    print("Male on female: {}".format(male_on_female_count))
    print("Female on male: {}".format(female_on_male_count))    
    print("White on minority: {}".format(white_on_minority_count))
    
    
def get_data(L):
    """
        Goes through file and counts differences in race and gender
        Returns:  A list of formatted data from the file
        """
    #initiate all variables
    white_count = 0
    black_count = 0
    hispanic_count = 0
    male_count = 0
    female_count = 0
    minority_on_white_count = 0
    white_on_minority_count = 0
    male_on_female_count = 0
    female_on_male_count = 0
    total_count = 0
    #Loops through data for each execution
    for item in L:
        #Count number of people of each race
        if "white" in item[0].lower():
                white_count += 1
        elif "black" in item[0].lower():
                black_count += 1 
        elif "hispanic" in item[0].lower():
                hispanic_count += 1
        minority_count = black_count + hispanic_count  

        #Count number of male, number of female
        if "female" in item[1].lower():
                female_count += 1
        elif "male" in item[1].lower():
                male_count += 1
        
        #Check the differences
        if not (("Not Available" in item[0]) or ("Not Available" in item[1])\
        or ("Not Available" in item[2]) or (item[2] == "")):
            
            if not (item[0].lower() == "race"):
                total_count += 1
                
            if "white" in item[0].lower():
                if "black" in item[2].lower() or "hispanic" in item[2].lower():
                    white_on_minority_count += 1
            elif "black" in item[0].lower():
                if "white" in item[2].lower():
                    minority_on_white_count += 1
            elif "hispanic" in item[0].lower():
                if "white" in item[2].lower():
                    minority_on_white_count += 1
                    
            if "female" in item[1].lower():
                if "female" in item[2].lower():
                    pass
                elif "male" in item[2].lower():
                    female_on_male_count += 1
            elif "male" in item[1].lower():
                if "female" in item[2].lower():
                    male_on_female_count += 1 
      
    print_data(white_count, black_count, hispanic_count, minority_count,\
    male_count, female_count, minority_on_white_count, white_on_minority_count\
    , male_on_female_count, female_on_male_count, total_count)

                    
#Gets data from the file in the form of a list, then inputs that data to 
#get_data
total_list = read_file()
get_data(total_list)

# Questions
# Q1: 5
# Q2: 7
# Q3: 2
# Q4: 7