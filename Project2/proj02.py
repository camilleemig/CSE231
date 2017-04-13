###########################################################
    #  Computer Project #2
    #
    #  Algorithm
    #    prompt for an integer, repeat until positive integer is given
    #    loops until the final output integer is less than 10 
    #       sets the total for this loop to 0       
    #       loops until all digits have been added to total integer
    #           adds the last digit of the number to total int
    #           gets the next digit or ouput the last digit
    #           gets rid of the digit that was just added
    #       prints the total int from that loop
    #       sets input_int to total_int to prepare for possible next loop
###########################################################
input_int = 0
total_int = 10

#Keeps prompting until it receives a positive int
while input_int <= 0:
    input_str = input("Please input a number: ")
    input_int = int(input_str)

#Loops until the total is less than 10
while total_int >= 10:
    total_int = 0
    #Loops until all numbers have been added to total    
    while input_int != 0:
        #Adds next digit to total
        total_int += input_int % 10
        #Checks if it is the last number and prints accordingly
        if input_int >= 10:
            print(input_int % 10, end=" + ")
        else:
            print(input_int % 10, end=" = ")
        input_int = input_int // 10
    print(total_int)
    input_int = total_int