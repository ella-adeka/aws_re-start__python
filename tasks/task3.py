# 3. Write a function that accepts an list of positive integers and returns an list of all prime numbers from the given list. 
# A prime number is a number that is only divisible by 1 and itself.

# create a list of numbers
primeList = [ 1, 2, 7, 11, 12, 14, 29, 42, 41, 5 ]

# define a function with arr as a parameter
def checkPrime(arr):
    # initialize a list to pass the prime numbers
    rePrimedlist = []

    # for each number in the arr
    for num in arr:

        for i in range(2, num):
            if (num % i) != 0:
                #  check if the number divided by i doesn't have a remainder of 0
                # append num to the new list of prime numbers
                rePrimedlist.append(num)
                # break as the condition is fulfilled
                break
    return rePrimedlist

print(checkPrime(primeList))