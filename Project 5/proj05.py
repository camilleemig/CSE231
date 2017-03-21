###########################################################
    #  Computer Project #5
    #
    #  Algorithm
    #   Call a function to prompt for a file name until one opens properly
    #   Call a function to read the wanted data into a list
    #   Call a function to find the average for every year
    #   Call a function to display the graph for the year
    #   Print the data for the graph
    #   Call a function to prompt for a month
    #   Call a function to get the month data from every year
    #   Call a function to display the graph for the month      
    #   Print the data for the graph    
    ###########################################################
import pylab

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
    fp = open_file()
    lines = []
    usable_data = []
    for line in fp:
        lines.append(line.split())
    for item in lines:
        converter = item[-3:]
        converter[0] = int(converter[0])
        converter[1] = int(converter[1])
        converter[2] = float(converter[2])
        usable_data.append(tuple(converter))
    fp.close()
    return usable_data

def get_month():
    """
        Prompts for a month as an integer until one works
        Returns:  The month as an integer and a string
        """
    while True:
        try:
            month_str = input("Enter a month (1-12): ")
            month = int(month_str)
            if month > 12 or month < 1:
                print("Integer is out of range")
                continue
            break
        except ValueError:
            print("Error. Not an Integer")
    months_list = ["January", "February", "March", "April", "May",\
    "June", "July", "August", "September", "October", "November", "December"]
    month_str = months_list[month-1]
    return month, month_str

def annual_average(L):
    """
        Creates a list of annual averages
        L: A list of all of the data from the file
        Returns:  A list of the annual averages
        """
    transfer_year = [0,0]
    annual_total_list = []
    annual_average_list = []

    #Makes a list of tuples of years and values
    for item in L:
        transfer_year[0] = item[0]
        transfer_year[1] = item[2]
        annual_total_list.append(tuple(transfer_year))

    #Calculates the average for each year and appends to a list of averages
    current_year = annual_total_list[0][0]
    summation = 0
    for item in annual_total_list:
        if current_year == item[0]:
            summation += item[1]
        else:
            average = summation/12
            transfer_year[0] = current_year
            transfer_year[1] = average
            annual_average_list.append(tuple(transfer_year))
            summation = 0
            current_year += 1
            summation += item[1]
    #Calculates the average from the last year
    average = summation/12
    transfer_year[0] = current_year
    transfer_year[1] = average
    annual_average_list.append(tuple(transfer_year))

    return annual_average_list

def month_average(L, month):
    """
        Creates a list of averages from each year of month m
        L: A list of all of the data from the file
        month: the month to get the averages for
        Returns: A list of the averages for month m from each year
        """
    transfer_month = [0,0]
    month_average_list = []
    for item in L:
        if item[1] == month:
            transfer_month[0] = item[0]
            transfer_month[1] = item[2]
            month_average_list.append(tuple(transfer_month))
    return month_average_list

def split_lists(L):
    """
        Splits a list into two lists
        L: The list to split
        Returns: A list of all of the data in the first column
                and a list of all of the data in the second column
        """
    lst1 = []
    lst2 = []
    for item in L:
        lst1.append(item[0])
        lst2.append(item[1])
    return lst1, lst2

def draw_plot( x, y, plt_title, x_label, y_label):
    ''' Draw x vs. y (lists should have the same length)
    Sets the title of plot and the labels of x and y axis '''

    pylab.title(plt_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)

    pylab.plot( x, y )
    pylab.show()
#Gets a list of all the data
full_list = read_file()

#Gets data for annual graph
annual_list = annual_average(full_list)
annual_year_list, annual_value_list = split_lists(annual_list)
annual_title = "Annual Average Flow From " + str(annual_year_list[0]) + " to "\
+ str(annual_year_list[-1])
draw_plot(annual_year_list, annual_value_list, annual_title, "Year", "Flow")
print("Annual Average Flow")
print("{:<8}{:>8}".format("Year", "Flow"))
for i in range(len(annual_year_list)):
    print("{:<8.0f}{:8.2f}".format(annual_year_list[i], annual_value_list[i]))

#Gets data for month graph
month, month_str = get_month()
month_list = month_average(full_list, month)
month_year_list, month_value_list = split_lists(month_list)
month_title = "Annual Average Flow for " + month_str
draw_plot(month_year_list, month_value_list, month_title, "Year", "Flow")
print("Annual Average Flow for", month_str)
print("{:<8}{:>8}".format("Year", "Flow"))
for i in range(len(month_year_list)):
    print("{:<8.0f}{:8.2f}".format(month_year_list[i], month_value_list[i]))

# Questions
# Q1: 6
# Q2: 5
# Q3: 1
# Q4: 6
