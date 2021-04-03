# prompt user to enter number / test if even or odd

input = input("Enter a number: ") # input function returns a string that needs to be converted to an integer
number = int(input)               # convert the string to an integer using the "int" constructor             


                          # if number is a multiple of 2 then print 1st line of code, else print 2nd line of code
if number % 2 == 0:       # the % operator returns the remainder when you divide the first number by the second, here we' re computing the remainder when number is divide by 2
    print("Your number is even.")
else:
    print("Your number is ood.")