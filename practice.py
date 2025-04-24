# print("Hello, World!")

#calaulate the sum of two numbers entered by the user
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# print(num1 + num2)

#check if a number is even or odd
# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("odd")

#calculate the factorial of a given number
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# num = int(input("Enter the given number:"))
# print("Factorial:", factorial(num))
      
#find the largest number of three numbers entered by the user
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# num3 = int(input("Enter the third number")
# Highest_number = max(num1, num2, num3)
# print(Highest_number)

#all even numbers from 1 to 20
# for i in range(2,21):
#    if i % 2 == 0:
#     print(i)

#sum of numbers from 1 to a given number
# num = int(input("Enter the number: "))
# sum_result = sum(range(1, num + 1))
# print(sum_result)

#check if a string is palindrome
# def is_palindrome(s):
#     return s == s[::-1]
# string = input("Enter a string: ")
# if is_palindrome(string):
#     print("This string is palindrome")
# else:
#     print("This string is not palindrome")

#count the number of vowels in a given string
# def count_vowels(s):
#   vowels = "aeiouAEIOU"
#   return sum(1 for char in s if char in vowels)
# string = input("Enter the string: ")
# print(count_vowels(string))

#reverse the list
# my_list = [2, 4, 6, 8]
# my_list.reverse()
# print(my_list)

#remove duplicate from a list
# my_list = [1, 2, 2, 4, 4, 3, 4, 3]
# newlist = set(my_list)
# print(newlist)

#convert a string to uppercase
# string = ("My name is Ifeoluwa.")
# upper_string= string.upper()
# print(upper_string)

#calculate the area of a circle with a given radius
# import math
# radius = int(input("Enter the radius: "))
# area_of_circle = math.pi * radius ** 2
# print(area_of_circle)

#replace all occurences of a character in a string
# string = "hello, world"
# new_string = string.replace('l', 's')
# print(new_string)

#maximum element in a list
# list = [5, 9, 3, 6]
# new_list = max(list)
# print(new_list)

#square root of a given number
# num = int(input("Enter the number: "))
# sqrt = num ** 0.5
# print(sqrt)

#check if two strings are anagrams
# def are_anagrams(str1, str2):
#     return sorted (str1) == sorted(str2)
# str1 = "silent"
# str2 = "listen"
# if are_anagrams(str1, str2):
#     print("They are anagrams")
# else:
#     print("They are not anagrams")

#check if a list is empty
# list = []
# if not list:
#     print("empty")
# else:
#     print("Not empty")

#find the length of the longest word in a given sentence
# sentence = input("Enter the sentence: ")
# def longest_word(sentence):
#     words = sentence.split()
#     longest = max(words, key=len)
#     return longest, len(longest)
# print(longest_word)

#check if a given number is a perfect square
# num = input("Enter the number: ")
# def is_perfect_square(n):
#     root = math.isqrt(n)  
#     return root * root == n
#     if is_perfect_square:
#         print("It is a perfect square")
#     else:
#         print("It is not a perfect square")

#common element between two lists
# list1 =[1, 2, 3, 4, 5, 6, 7]
# list2 =[4, 5, 6, 7, 8, 9, 0]
# common = list(set(list1) & set(list2))
# print(common) 

#capitalize the first letter of each word in a sentence
# sentence = "my name is ifeoluwa"
# capitalized = sentence.title()
# print(capitalized) 

#Calculate the multiplication and sum of two numbers
# int1 = 50
# int2 = 30
# if (int1 * int2)<= 1000:
#     print(int1 * int2)
# else:
#     print(int1 + int2)

# Print the Sum of a Current Number and a Previous number
# num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# numbers = iter(num)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

#Write a program that adds two numbers input by the user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(num1 + num2)

#Calculate the area and perimeter of a rectangle.
# import math
# length = 2
# breadth = 3
# area_of_rectangle = length * breadth
# print(area_of_rectangle)
# perimeter_of_rectangle = 2 * (length + breadth)
# print(perimeter_of_rectangle)

#Swap the values of two variables
# var1 = 3
# var2 = 5
# var1, var2 = var2, var1

# print("var1 =", var1)
# print("var2 =", var2)\

#Calculate the factorial of a number
# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers.")
# elif num == 0:
#     print("The factorial of 0 is 1.")
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")

#Print all even numbers between 1 and 100.
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# Ask the user for a number n and print all prime numbers from 1 to n
# n = int(input("Enter a number: "))
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def print_primes_up_to_n(n):
#     print(f"Prime numbers from 1 to {n}:")
#     for i in range(1, n + 1):
#         if is_prime(i):
#             print(i, end=" ")
#     print()
# print_primes_up_to_n(n)

# 