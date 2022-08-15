# 9. Write a function that takes a string and determines if the string is a palindrome. 
# A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, 
# such as madam, racecar. The function should return "Yes" if the word is a palindrome and "No" if it isn't. 
# **You are not to use the programming language's existing function or method, if any**.

# ask the question to get input
palinStr = input("Check palindrome: ")

# define a function that teakes text as a parameter
def checkPalindrome(text):
    # set isPalindrome to false(initialization)
    isPalindrome = False
    # the reversed string will be output of the string reversed
    reverseStr = text[::-1]

    # if the reversed String is equal to the original text
    if (reverseStr == text):
        # it is a palindrome
        isPalindrome = True
        print("yes")
    else:
        # else, it is not
        isPalindrome = False
        print("no")

    # check state of palindrome and return values based on the state
    if isPalindrome == True:
        return "{} is a palindome".format(reverseStr)
    else:
        return "{} is not a palindome".format(reverseStr)

print(checkPalindrome(palinStr))