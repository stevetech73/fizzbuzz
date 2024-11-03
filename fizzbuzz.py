# add your code here
count = 0

for count in range(1, 101):
    
    if count > 100:
        print("Done")
        exit()
    else:    
        if count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print ("Buzz")
        elif count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        else:
            print(count)
        