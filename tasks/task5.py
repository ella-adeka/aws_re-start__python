# 5. Write a method to replace all spaces in a string with '%20';.

# create a variable with input to ask the question
myQuestionToReplace = input("What's your favorite movie?")
# replace any spaces in myQuestionToReplace with %20
toReplace = myQuestionToReplace.replace(" ", "%20")
# print the answer to the input without the spaces
print(toReplace)