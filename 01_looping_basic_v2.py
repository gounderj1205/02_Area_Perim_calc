# checks that usrs enter a number that is more than zero
valid = False
while not valid:


   try:
   
        # ask user to enter a number
        response = float(input("enter a number: "))

        # checks number is more thatn zero
        if response > 0:
            valid = True

        # outputs error if input is invalid
        else:
            print("please enter a number that is more than zero")
            print()

     except ValueError:
        print


    




        

 
         
    

