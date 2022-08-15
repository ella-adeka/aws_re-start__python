# 1. Write a function that takes an list of positive integers. The function should calculate the sum of all even and odd integers and 
# return an list containing the sums. The first index in the returned list should hold the sum of the even integers and the second index 
# should hold the sum of the odd integers.

# create a list of numbers
posIntList = [1,10,4,3,9,2,15,8,6,5]

# define a function to check a list for even and odd numbers, with arr as the parameter
def checkEvenOrOdd(arr):
    # initialize variables to add values to them
    evenNums = 0
    oddNums = 0

    # for each number in list
    for num in arr:
        # check if the number divided by 2 has a remainder of 0
        if(num%2 == 0):
            # If it has a remainder of 0, it is even, add it evenNums
            evenNums+=num
        else:
            # else,it is odd, add to oddNums
            oddNums +=num
    print("sum of even numbers: ", evenNums)
    print("sum of odd numbers: ", oddNums)
    # return a list of the sum of the even numbers and the sum of the odd numbers
    return [evenNums, oddNums]

# pass list as argument
print(checkEvenOrOdd(posIntList))