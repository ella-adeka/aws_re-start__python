# NVIT_NGBEN4_PythonAssignment1
An assignment in python programming for students of NVIT reStart program at New Vision Institute of Technology

#  Technical Tasks

## Tasks

1. Write a function that takes an list of positive integers. The function should calculate the sum of all even and odd integers and return an list containing the sums. The first index in the returned list should hold the sum of the even integers and the second index should hold the sum of the odd integers.

2. Write a function that accepts a positive integer and determines if it is a prime number. The function should return true if it is a prime number or false if it isn't.

3. Write a function that accepts an list of positive integers and returns an list of all prime numbers from the given list. A prime number is a number that is only divisible by 1 and itself.

4. Create a password validator function that takes in the password as its argument and returns an integer value you can evaluate to determine the password strength. Using the following validators:
 0 -\&gt; very weak e.g. a password with only strings
 1 -\&gt; weak e.g. a password with only numbers
 2 -\&gt; strong e.g. a password containing strings and numbers
 3 -\&gt; very strong e.g. a password containing strings, numbers and special characters (!,@,#,$,%, etc)

5. Write a method to replace all spaces in a string with '%20';.
 Example:

    **Input** : "Mr John Smith "

    **Output** : "Mr%20John%20Smith"

6. Write a function that takes two parameters, an list and some number. The function should determine whether any three numbers in the list add up to the number. If it does, the function should return the numbers as an list. If it doesn't, the function should return -1.
 Example
**Input** : [1, 2, 3, 4, 5, 6], 6
**Output** : [1, 2, 3]

7. Write a function that takes an list of positive integers and calculates the standard deviation of the numbers. The function should return the standard deviation.

8. Write a method to count the number of 3s that appear in all the numbers between 0 and n (inclusive). It should return an object containing the count of the number of 3s that appear and an list of the numbers that have 3s in them
 Example:
**Input** : 35
**Output** : { count: 10, numbers: [3, 13, 23, 30, 31, 32, 33, 34, 35] }

9. Write a function that takes a string and determines if the string is a palindrome. A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam, racecar. The function should return "Yes" if the word is a palindrome and "No" if it isn't. **You are not to use the programming language's existing function or method, if any**.

10. Write a function that takes a string. The function should calculate the character in the string with the most occurrences and return that character and the total occurrence of the character in a dictionary. If more than one character has the most occurrence, return those characters and total occurrences of each as an list of maps or JSON objects.
 Example
**Input** : "afhuusnimr443o0sggg"
**Output** : "g"

## Bonus Tasks

### Bonus 1:

Building

| BuildingID | int |
| --- | --- |
| ComplexID | int |
| BuildingName | varchar(100) |
| Address | varchar(100) |

Apartments

| AptID | int |
| --- | --- |
| UnitNumber | varchar(10) |
| BuildingID | int |

Requests

| RequestID | int |
| --- | --- |
| Status | varchar(100) |
| AptID | int |
| Description | varchar(100) |

Complexes

| ComplexID | int |
| --- | --- |
| ComplexName | varchar(100) |

Tenants

| TenantID | int |
| --- | --- |
| TenantName | varchar(100) |

AptTenants

| TenantID | int |
| --- | --- |
| AptID | int |

Given the above SQL tables, write a query that:

1. Gets a list of tenants who are renting more than one apartment.
2. Write a SQL query to get a list of all buildings and the number of open requests (Requests in which status equals 'Open').

### Bonus 2:

This challenge asks you to take a string composed of only lowercase letters and space characters, for example, "_hello world_" and replace every consonant in the string with the next consonant in the alphabet. So in the above example, the output should be "_jemmo xosmf_" and you can see that we left every vowel in place and only changed the consonants. You should notice that the last letter changed was from "d" to "f" and not from "d" to "e" because "e" is a vowel.


## Instructions

1. You can develop your solutions using your preferred programming/scripting language, python is preferred.
2. Complete at least any 5 questions. However, you are expected to attempt all 10 questions.
3. You are encouraged to attempt the bonus questions. Solving the bonus questions gives additional points.
4. Do not copy solutions from the Internet, books or seek help elsewhere (this will be embarrassing when you are asked to explain your code).
5. Comment every step in your code.
6. You have to be comfortable explaining your solution after submitting your work via a video/audio call.
7. Upload your submission to your GitHub account. If you do not have one, you are required to create one ([www.github.com](http://www.github.com/)).
8. When submitting your solution, ensure that each question is submitted in its own file with the following naming convention: _Task\_1.js_, _Task\_2.js_,..., _Bonus\_Task\_1_, _Bonus\_Task\_2_.




Courtesy of Basecamp from Wootlab 
