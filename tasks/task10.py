# 10. Write a function that takes a string. 
# The function should calculate the character in the string with the most occurrences and return that character and the total occurrence 
# of the character in a dictionary. If more than one character has the most occurrence, 
# return those characters and total occurrences of each as an list of maps or JSON objects.

# create a variable with string to be checked as value
tobeChecked = "Time after time"
print(tobeChecked)

# define a function with one parameter
def checkTheMost(strMost):
    # initialize empty dictionary
    occurences = {}

    # for item in lowercase parameter
    # remove empty spaces with replace()
    for i in strMost.lower().replace(" ", ""):
        # if item in occurences dict, add 1 to its previous value in the diictionary
        if i in occurences:
            occurences[i]+=1
        else:
            # else, if item occurs only once, set the value to 1
            occurences[i]=1
    # return occurences dictionary
    return occurences


# pass the string variable as an argument to the function
print(checkTheMost(tobeChecked))