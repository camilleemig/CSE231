###########################################################
    #  Computer Project #6
    #
    #  Algorithm
    #   Call a function to prompt for file names until they open properly
    #   Call a function to adds data from all files to total_dict        
    #   Call a function to get wanted data from the full dictionary of data
    #   Call a function to get the years and averages    
    #   Call a function to plot the graphs
    #   Print the averages for city/highway data
    ###########################################################
import csv
import pylab
import matplotlib.patches as patches

def open_files():
    """
    Opens files from user input.
    Returns: List of file pointers
    """
    
    file_list = []
    while True:
        try:
            decades = input("Input multiple decades separated by commas," +\
            " e.g. 1980, 1990, 2000:").split(",")
            
            #Checks to see if it is a valid decade
            for index,year in enumerate(decades):
                if year.strip() == "1980": 
                    fp1980 = open(year.strip()+"s.csv")
                    file_list.append(fp1980)
                elif year.strip() == "1990":      
                    fp1990 = open(year.strip()+"s.csv")
                    file_list.append(fp1990)
                elif year.strip() == "2000":            
                    fp2000 = open(year.strip()+"s.csv")
                    file_list.append(fp2000)
                elif year.strip() == "2010":            
                    fp2010 = open(year.strip()+"s.csv")
                    file_list.append(fp2010)
                else:
                    print("Error in decade " + '"' + str(year) + '"')
                    
            #If there are still no files loop again, otherwise break and return
            if file_list == []:
                continue
            else:
                break
        #If the file name was valid but it could not be found, print this
        except FileNotFoundError:
            for item in file_list:
                item.close()
            print("File Not Found")
            continue
    return file_list

def read_file(file):
    """
    Reads the file and makes a dictionary of manufacturer, years, city mileage
        and highway mileage
    Returns: dictionary of data from file
    """
    
    dictionary = {}
    csv_fp = csv.reader(file)
    #L[46] = manufacturer, L[63] = year
    #L[4]= city mileage, L[34]=highway mileage
    for line in csv_fp:
        #Skip the headings and the year 2017
        if (not (line[46] == 'make')) and (not (line[63] == '2017')):
            if line[46] in dictionary:
                #Add the city and highway mileage if the year has been made
                if line[63] in dictionary[line[46]]:
                    dictionary[line[46]][line[63]][0] += [int(line[4])]
                    dictionary[line[46]][line[63]][1] += [int(line[34])]
                #Add the year and data if it was not made previously
                else:
                    dictionary[line[46]][line[63]] = [[int(line[4])],\
                    [int(line[34])]]
            #Adds a new manufacturer
            else:
                dictionary[line[46]] = {line[63]:[[int(line[4])],\
                [int(line[34])]]}
    return dictionary
    
    
def merge_dict(target, source):
    """
    Merges two dictionaries
    Source: Dictionary to get data from
    Target: Dictionary to add data to
    Returns: updated dictionary (target)
    """
    
    #If the target is empty, just copy the source
    if target == {}:
        target = source
    #Else loop through each key and update the target key with the source info
    else:
        for manufacturer in source:
            if manufacturer in target:
                target[manufacturer].update(source[manufacturer])
            else:
                target[manufacturer] = source[manufacturer]

    return target

def get_wanted_data(wanted_data_dict, total_dict):
    """
    Sorts through full dictionary for wanted companies
    total_dict: Dictionary with every manufacturer
    wanted_data_dict: Empty dictionary with wanted companies initialized
    Returns: 
    """
    #Lists to check if it is a wanted manufacturer
    Ford = ['Ford', 'Mercury', 'Lincoln']
    GM = ['GMC','Chevrolet', 'Pontiac', 'Buick', 'Cadillac', 'Oldsmobile',\
    'Saturn']
    Toyota = ['Toyota', 'Lexus', 'Scion']
    Honda = ['Honda', 'Acura']
    
    #Loop through each key in total_dict
    for manufacturer in total_dict:
        if manufacturer in Ford:     
            company = 'Ford'            
        elif manufacturer in GM: 
            company = 'GM'
        elif manufacturer in Toyota:
            company = 'Toyota'
        elif manufacturer in Honda:
            company = 'Honda'
        else:
            #Skips any manufacturer that isn't wanted
            continue
        #Adds the data from each year to wanted_data_dict
        for year in total_dict[manufacturer]:
            if year in wanted_data_dict[company]:
                wanted_data_dict[company][year][0] += total_dict[manufacturer]\
                [year][0]
                wanted_data_dict[company][year][1] += total_dict[manufacturer]\
                [year][1]
            else:
                wanted_data_dict[company][year] = total_dict[manufacturer]\
                [year]
    return wanted_data_dict 

def get_averages(full_dict):
    converter_dict = {}
    city_dict = {}
    hwy_dict = {}
    years = []
    
    #For each manufacturer, calculate the averages and add them to a list, then
    #sort the list. Finally, add the list to a dictionary with the key as the
    #manufacturer
    for manufacturer in full_dict:
        converter = []
        for year in full_dict[manufacturer]:
            city_average = round(sum(full_dict[manufacturer][year][0])/\
            len(full_dict[manufacturer][year][0]), 2)
            hwy_average = round(sum(full_dict[manufacturer][year][1])/\
            len(full_dict[manufacturer][year][1]), 2)
            converter.append([year, city_average, hwy_average])
        converter.sort()
        converter_dict[manufacturer] = converter
        
    #For each company in the dictionary, add the data to a city dictionary,
    #hwy dictionary, and year list
    for company in converter_dict:
        for year in converter_dict[company]:
            if not (year[0] in years):
                years.append(year[0])
            if company in city_dict:
                city_dict[company] += [year[1]]
            else:
                city_dict[company] = [year[1]]
            if company in hwy_dict:
                hwy_dict[company] += [year[2]]
            else:
                hwy_dict[company] = [year[2]] 
                
    return years, city_dict, hwy_dict 
       
def plot_mileage(years,city,highway):
    '''Plot the city and highway mileage data.
       Input: years, a list of years;
              city, a dictionary with manufacturer as key and list of annual
              mileage as value;
              highway, a similar dictionary with a list of highway mileage as
              values;
       Requirement: all lists must be the same length.'''
    pylab.figure(1)
    pylab.plot(years, city['Ford'], 'r-', years, city['GM'], 'b-', years,
             city['Honda'], 'g-', years, city['Toyota'], 'y-')
    red_patch = patches.Patch(color='red', label='Ford')
    blue_patch = patches.Patch(color='blue', label='GM')
    green_patch = patches.Patch(color='green', label='Honda')
    yellow_patch = patches.Patch(color='yellow', label='Toyota')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('City Fuel Economy (MPG)')
    pylab.show()
    
    # Plot the highway mileage data.
    pylab.figure(2)
    pylab.plot(years, highway['Ford'], 'r-', years, highway['GM'], 'b-', years,
             highway['Honda'], 'g-', years, highway['Toyota'], 'y-')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('Highway Fuel Economy (MPG)')
    pylab.show()
    
    
#Open files
files = open_files()
#Error checking to make sure there are files to open
if files == None:
    print("Program ending.")
else:    
    #Adds all data from all files to total_dict
    total_dict = {}
    for file_input in files:
        decade_dict = read_file(file_input)
        total_dict = merge_dict(total_dict, decade_dict)
        
    #Gets wanted data from the full dictionary of data
    manufacturer_dict = {'Ford':{}, 'GM':{}, 'Toyota':{}, 'Honda':{}}
    wanted_manufacturers_dict = get_wanted_data(manufacturer_dict, total_dict)
    
    #Get the years and averages
    years_dict, city_averages_dict, hwy_averages_dict = get_averages\
    (wanted_manufacturers_dict)
    
    #Plot the graphs
    plot_mileage(years_dict,city_averages_dict,hwy_averages_dict)
    
    #Print the averages for city data
    print("City")
    print("{:>11}  {:5}".format("Company:", "Mileage"))    
    for manufacturer in city_averages_dict:
        city_avg = sum(city_averages_dict[manufacturer])/\
        len(city_averages_dict[manufacturer])
        print("{:>10}: {:3.2f}".format(manufacturer, city_avg))
    #Print the averages for highway data
    print("Highway")
    print("{:>11}  {:5}".format("Company:", "Mileage"))    
    for manufacturer in hwy_averages_dict:
        hwy_avg = sum(hwy_averages_dict[manufacturer])/\
        len(hwy_averages_dict[manufacturer])
        print("{:>10}: {:3.2f}".format(manufacturer, hwy_avg))

# Questions
# Q1: 6
# Q2: 5
# Q3: 2
# Q4: 7