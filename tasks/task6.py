# 6. Write a function that takes two parameters, an list and some number. 
# The function should determine whether any three numbers in the list add up to the number. 
# If it does, the function should return the numbers as an list. If it doesn't, the function should return -1.
# **Input** : [1, 2, 3, 4, 5, 6], 6
# **Output** : [1, 2, 3]

# create the list of numbers
firstThreeList = [1, 9, 8, 3, 5]

# define a function that takes the array and a number as parameters
def checkFirstThree(arr, num):
    # initialize the variable
    firstThreeArr = 0

    # for each element in the first three elements in the array
    for i in arr[0:3]:
        # add it to the initialized variable
        firstThreeArr+=i
        # check if the sum of these three numbers are equal to the num parameter
        if(firstThreeArr == num):
            print(arr[0:3])
            break
    else: 
        # if the sum is not equal to the num parameter, set the initialized variable to -1
        firstThreeArr = -1
        print("first three numbers do not sum up")
    # return the value of the variable
    return firstThreeArr

# call the function with the array and number as arguments
print(checkFirstThree(firstThreeList, 20))