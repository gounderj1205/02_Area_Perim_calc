# functions go here

# checks input is a number more thatn zero
def num_check(question):

    valid = False
    while not valid:

        error = "please enter a number that is more than zero"
        
        try:
    
            # ask user to enter a number
            response = float(input(question))

            # checks number is more thatn zero
            if response > 0:
                return response

            # outputs error if input is ivalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Main Routine goes here

# Introduction / heading print statements
print()
print("**** Area perimeter calculator *****")
print()

keep_going = ""
while keep_going == "":

    width = num_check("width: ")
    height = num_check("height: ")
    price_per_metre = num_check("price per metre: $")
    

    # calculate perimeter (width x height)
    perimeter = 2 * (width + height)

    
    # calculate cost of fencing
    cost_of_fencing = perimeter * price_per_metre
    # Output area and perimeter4
    print("perimeter: {:.2f} units" .format(perimeter)) 
    print("cost of fencing: $ {:.2f} " .format(cost_of_fencing))
    print()

    keep_going = input ("press <enter> to keep going or any key to quit")

print()
print("thanks for using the area / perimeter calculator")  



print()
print("-" * 30)
print()






  
 
      

 
         
    

