###########################################################
    #  Computer Project #4
    #
    #  Algorithm
    #    Call a function to prompt for a file name until one opens properly
    #       Return the open file
    #    Call a function to get lines 9 and 44 from the file
    #       Return lines 9 and 44
    #    Call a function to find the minimum percentage
    #       Return the minimum value and its index
    #    Call a function to find the maximum percentage
    #       Return the maximum value and its index
    #   Call a function to find the minimum GDP
    #       Input the index of the minimum percentage to get the value       
    #       Return the minimum GDP    
    #   Call a function to find the maximum GDP
    #       Input the index of the maximum percentage to get the value       
    #       Return the maximum GDP
    #   Call a function to use the index of the minimum percentage to 
    #       find the year
    #   Call a function to use the index of the maximum percentage to 
    #       find the year
    #   Call a function to display the minimum change in GDP, the year in which
    #       it occurred, and the minimum GDP
    #       then display the the maximum change in GDP, the year in which
    #       it occurred, and the maximum GDP
    ###########################################################

#All variables are integers or floats unless otherwise stated

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

def get_lines(file):
    """
        Extracts the ninth and fourty-fourth lines from the input file
        file: the file to get lines from
        Returns: the ninth and fourty-fourth lines as two strings
        """
    count = 1
    for line_str in fp:
        if count == 9:
            line_nine_str = line_str
        elif count == 44:
            line_fourty_four_str = line_str
            break
        count += 1
    return line_nine_str, line_fourty_four_str

def find_min_percent(line):
    """
        Finds the minimum change in gdp in a line of data
        line: the line to get the minimum value from
        Returns: the minimum change and its index, as a float and integer
        """
    minimum = 100000
    minimum_index = 0
    i = 0
    while i <= 46:
        #(76 + i*12) returns the index because the first number starts at 76
        #and each number is 12 characters long
        current_number = float(line[(76 + i*12):(76 + (i + 1)*12)].strip())
        if current_number < minimum:
            minimum = current_number
            minimum_index = (76 + i*12) 
        i += 1
    return minimum, minimum_index
    
def find_max_percent(line):
    """
        Finds the maximum change in gdp in a line of data
        line: the line to get the maximum value from
        Returns: the maximum change and its index, as a float and integer
        """
    maximum = -100000
    maximum_index = 0
    i = 0
    while i <= 46:
        current_number = float(line[(76 + i*12):(76 + (i + 1)*12)].strip())
        if  current_number > maximum:
            maximum = current_number
            maximum_index = (76 + i*12) 
        i += 1
    return maximum, maximum_index

def find_gdp(line, index):
    """
        Finds the gdp related to the index of the gdp change
        line: the line to get the gdp value from
        index: the index at which the gdp can be found (int)
        Returns: the gdp related to the index of the gdp change (float)
        """
    gdp = float(line[(index):(index + 12)].strip())  
    return gdp

def find_year(index):
    """
        Calculates the year related to the index of the GDP
        index: the index at which the gdp can be found (int)
        Returns: the year related to the index (int)
        """
    #(index-76)/12 because the first gdp starts at character 76, and each is
    #twelve characters long
    year = (index-76)/12
    year += 1969
    return year

def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    """
        Displays the data formatted properly in a string
        min_val: The minimum change in GDP (float)
        min_year: The year at which the minimum GDP occurred (int)
        min_val_gdp: The minimum GDP (float)
        max_val: The maximum change in GDP (float)
        max_year: The year at which the maximum GDP occurred (int)
        max_val_gdp: The maximum GDP (float)
        Returns: None
        """
        
    print("\nGross Domestic Product")
    
    print("The minimum change in GDP was "\
    "{:.1f} in {:.0f} when the GDP was {:.2f} trillion dollars.".format(\
    min_val, min_year, min_val_gdp/1000))
    
    print("The maximum change in GDP was "\
    "{:.1f} in {:.0f} when the GDP was {:.2f} trillion dollars.".format(\
    max_val, max_year, max_val_gdp/1000))


fp = open_file()

line_nine_str, line_fourty_four_str = get_lines(fp)

min_change, index_min = find_min_percent(line_nine_str)
max_change, index_max = find_max_percent(line_nine_str)

min_gdp = find_gdp(line_fourty_four_str, index_min)
max_gdp = find_gdp(line_fourty_four_str, index_max)

min_year = find_year(index_min)
max_year = find_year(index_max)

display(min_change, min_year, min_gdp, max_change, max_year, max_gdp)

fp.close()

# Questions
# Q1: 5
# Q2: 2
# Q3: 2
# Q4: 6