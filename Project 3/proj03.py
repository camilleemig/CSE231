###########################################################
    #  Computer Project #3
    #
    #  Algorithm
    #    prompt for resident status
    #    prompt for College level
    #    prompt for college if junior, senior, or graduate
    #    prompt for credits, convert to int
    #    add to bill based on credits and year
    #    add to bill based on college and credits if junior or senior
    #    add special fees for graduate/undergraduate
    #    add special fees to every bill
###########################################################
#All variables are strings, other than credits, which is an integer.

print("Tuition Calculator")
calculate = 'yes'
while calculate == 'yes':
    bill = 0.0
    year = ''
    college = ''
    
    #Get resident status, convert to lowercase
    resident = input("Resident (Yes/No): ")
    resident = resident.lower()
    
    #Get year, convert to lowercase, upperclassman, get college
    year = input("Input level - freshman, sophomore, junior, senior, graduate"\
    ": ")
    year = year.lower()
    if year == "junior" or year == "senior" or year == "graduate":
        college = input("College - business, engineering, health, sciences, N"\
        "one: ")
        college = college.lower()
    else:
        college = "N/A"
    
    credits_int = int(input("Input credits this semester: ")) 
    
    #Check if student is a resident
    if resident == 'yes':    
        if year == "freshman" or year == "sophomore":
            bill += (credits_int * 468.75)
        elif year == "junior" or year == "senior":
            bill += (credits_int * 523.25)
        else:
            bill += (credits_int * 698.50)    
    #Run this if user is not a resident
    else:
        if year == "freshman" or year == "sophomore":
            bill += (credits_int * 1263.00)
        elif year == "junior" or year == "senior":
            bill += (credits_int * 1302.75)
        else:
            bill += (credits_int * 1372.00)  
    
    #Add the college fee if the student is a junior or senior or graduate
    #If-else for if part or full time student
    if credits_int <= 4:
        if college == "business":
            bill += 109.00
        elif college == "engineering":
            bill += 387.00
        elif college == "health":
            bill += 50.00
        elif college == "sciences":
            bill += 50.00
        if year == "graduate":
            bill += 37.50
    else:
        if college == "business":
            bill += 218.00
        elif college == "engineering":
            bill += 645.00
        elif college == "health":
            bill += 100.00
        elif college == "sciences":
            bill += 100.00
        if year == "graduate":
            bill += 75.00
    
    #Add undergrad/graduate fees        
    if year == "graduate":
        bill += 11.00
    else:
        bill += 18.00
    
    #Add fees that apply to every student
    bill += 3.00
    bill += 5.00
    
    print("Total bill: ${:,.2f}".format(bill))
    
    calculate = input("Do you want to calculate again (Yes/No): ")
    calculate = calculate.lower()
    
# Questions
# Q1: 6
# Q2: 3
# Q3: 1
# Q4: 6