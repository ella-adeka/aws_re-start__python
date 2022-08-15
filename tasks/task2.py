# 2. Write a function that accepts a positive integer and determines if it is a prime number. The function should return true 
# if it is a prime number or false if it isn't.

# create an input variable to check if a number is prime or not
primeQuestion = int(input("Write a number and I'll tell you if its prime or not: "))

# define a function with parameter num
def primeOrNot(num): 
    # set isPrime to False, since the number to be inputted is not known
    isPrime = False

    # A prime number is a number > 1
    if num > 1:

        for i in range(2, num):
        # for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                # check if the number divided by i has a remainder of 0
                # If yes, it is not a prime number
                isPrime = False
                print(num, "is a not prime number")
                break
        else:
            #  check if the number divided by i doesn't have a remainder of 0
            # If no, it is a prime number, set isPrime to True
            isPrime = True
            print(num, "is a  prime number")
    return isPrime

# pass the input variable as an argument
print(primeOrNot(primeQuestion))