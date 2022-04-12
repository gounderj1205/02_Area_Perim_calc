# functions go here

# checks input is a number more thatn zero
def num_check(question):

    valid = False
    while not valid:

        error = "please enter a number that is more than zero"
        
        try:
    
            # ask user to enter a number
            response = float(input("enter a number: "))

            # checks number is more thatn zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Main Routine goes here

keep_going = ""
while keep_going == "":

    width = num_check("width: ")
    height = num_check("height: ")

    # calculate area (width s height)
    area = width * height

    # calculate perimeter (width x height)
    perimeter = 2 * (width * height)

    # Output area and perimeter4
    print("perimeter: {} units" .format(perimeter)) 
    print("Area: {} square units" .format(area))
    print()

    keep_going = input ("press <enter> to keep going or any key to quit")

print()
print("thanks for using the area / perimeter calculator")    


  
 
        

 
         
    

