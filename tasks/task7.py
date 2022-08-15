# 7. Write a function that takes an list of positive integers and calculates the standard deviation of the numbers. 
# The function should return the standard deviation.

import math 
# import math, to use the square root method

# create a list of values
stdDevList = [1, 5, 2, 9, 2, 17, 23, 10, 4, 2]

# define a function with array as a parameter
def calcStdDeviation(arr):
    # initialize variables
    stdSum = 0
    stdMean = 0
    eachDeviation = []
    squareOfEachDeviation = []
    sumOfSquares = 0
    
    print("The original array: {}".format(arr))

    # Step 1: Calulate the mean of the lisr
    for i in arr:
        stdSum+=i
    # stdMean = stdSum/len(arr)
    stdMean = int(stdSum/len(arr))
    print("The mean is {}".format(stdMean))

    # Step 2: Find each list item's deviation from the mean
    for i in arr:
        eachDeviation.append(i - stdMean)
    print("Each item's deviation from the mean is {}".format(eachDeviation))

    # Step 3: Square each deviation from the mean
    for i in eachDeviation:
        squareOfEachDeviation.append(i**2)
    print("The square of each deviation from the mean is {}".format(squareOfEachDeviation))

    # Step 4: Find the sum of squares
    for i in squareOfEachDeviation:
        sumOfSquares += i
    print("The sum of squares is {}".format(sumOfSquares))

    # Find the variance
    # by dividing the squares by n-1
    variance = sumOfSquares/(len(arr) - 1)
    print("The variance is {:.2f}".format(variance))

    # Find the square root of the variance
    varianceSqrt = math.sqrt(variance)
    print("The square root of the variance is {:.2f}".format(varianceSqrt))
    
    return "Therefore, the standard deviation is {:.2f}".format(varianceSqrt)

print(calcStdDeviation(stdDevList))