# add your code here
count = 0      # set counter

for count in range(1, 101):      # define the range
    
    if count > 100:       # count is greater than 100
        print("Done")       
        exit()        # stop
    else:
        if count % 3 == 0 and count % 5 == 0:         # number is divisible by 3 and by 5
            print("FizzBuzz")    
        elif count % 3 == 0:       # number is divisible by 3
            print("Fizz")
        elif count % 5 == 0:      # number is divisible by 5
            print ("Buzz")
                
        else:
            print(count)
        
