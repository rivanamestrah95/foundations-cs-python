''' Write a function that takes an integer from the user and calculates its factorial, (Thefactorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n) Example 1: Input: 4, Output: 24 (1 * 2 * 3 * 4)
Example 2: Input: 6, Output: 720 (1 * 2 * 3 * 4 * 5 * 6)
Example 3: Input: 1, Output: 1
'''

def Factorial(number):
  fact = 1
  for i in range(1, number + 1):
    fact *= i
  return fact


print(Factorial(int(input("enter n1 for factorial: "))))


'''Write a function that takes an integer as an input from the user and finds all its divisors
and stores them in a list.
Example 1: Input: 10, Output: [1, 2, 5, 10]
Example 2: Input: 16, Output: [1, 2, 4, 8, 16]
Example 3: input: 5, Output: [1,5]
'''

def Divisors(num):
  list1 = []
  for i in range(1, num + 1):
    if num % i == 0:
      list1.append(i)
  return list1


print(Divisors(int(input("enter a num to check all divisors : "))))

'''Write a function called reverseString that takes a string as input from the user and returns
the string reversed. You must use a loop to implement the reversal, and you cannot use any
built-in string or list reversal functions.
Example 1: Input: “Hello World”, Output: “dlroW olleH”
Example 2: Input: “oneword”, Output: “droweno”
'''

def reverseString(word):
  for i in range(-1, -len(word) - 1, -1):
    print(word[i], end="")


reverseString(input("enter a word : "))

'''
Write a function that takes a list of integers as input from the user and returns a new list
containing only the even numbers from the original list, in the same order.
Example 1: Input: [1, 2, 3, 4, 5, 6], Output: [2, 4, 6]
Example 2: Input: [5, 3, 18, 4, 2, 7, 10], Output: [18, 4, 2, 10]
Example 3: Input: [5, 3, 11, 5, 1, 7, 27], Output: []
'''


def Even(list1):
  even = []
  for i in range(0, len(list1)):
    if list1[i] % 2 == 0:
      even.append(list1[i])
  return even


print(Even(eval(input("  enter a list of numbers : "))))


'''
5. Write a function that takes a string as input and checks whether it meets the requirements
for a strong password. A strong password should be at least 8 characters long, contain at
least one uppercase letter, one lowercase letter, one digit, and one special character (a
special character is either #, ?, !, $).
Example 1: Input: “Hello5?world” Output: “Strong password”
Example 2: Input: “password” Output: “Weak password”
Example 3: Input: “Password123” Output: “Weak password”
'''


def PasswordString(password):
  if (len(password) < 8):
    print("WEAK PASSWORD")
  else:
    upperLetter = False
    lowerLetter = False
    oneDigit = False
    specialLetter = False
    for i in password:
      if i.isupper():
        upperLetter = True
      elif i.islower():
        lowerLetter = True
      elif i.isdigit():
        oneDigit = True
      elif i in "#?!$":
        specialLetter = True
    if upperLetter and lowerLetter and oneDigit and specialLetter:
      return "Strong password"
    else:
      return "Weak password"


print(PasswordString(input("enter a password: ")))

