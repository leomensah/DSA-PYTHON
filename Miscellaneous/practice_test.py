
""" PRINT A NUMBER UP DOWN TO UP """
import math

def printNum(number):
    if number == 0:
        return
    printNum(number - 1)
    print(number)

"""PRINT A NUMBER DOWN TO UP"""
def printNumRev(number):
    if number == 0:
        return
    print(number, end=" ")
    printNumRev(number-1)

""" PRINT A NUMBER TOP DOWN AND UP DOWN """
def printNumBoth(number):
    if number == 0:
        return
    print(number, end=" ")
    printNumBoth(number-1)
    print(number, end=" ")

""" FACTORIAL OF A NUMBER """
def factFunction(number):
    if number <= 1:
        return 1
    return number * factFunction(number-1)

""" SUM OF 1 - N """
def sumOf1_N(number):
    if number <= 1:
        return 1
    return number + sumOf1_N(number-1)

""" SUM OF DIGITS """
def n_digits(nums):
    if nums == 0:
        return 0
    return (nums%10) + n_digits(nums // 10)

""" PRODUCT OF ELEMENTS IN A DIGITS"""
def prod_digits(num):
    if num%10 == num:
        return num
    return (num%10) * prod_digits(num//10)

""" REVERSE AN INTEGER """
def reverseANumber(number):
    def helper(number, digits):
        if number %10 == number:
            return number
        rem = number % 10
        return rem * (int)(math.pow(10, digits-1)) + helper(number // 10, digits-1)
    digits = (int)(math.log10(number)) + 1
    return helper(number, digits)

""" CHECK A PALINDROME """
def palindromeNumber(number):
    return number == reverseANumber(number)

""" COUNT ZEROS """
def zeros(digits):
    return countZeros(digits, 0)
def countZeros(digits, count):
    if digits == 0:
        return count
    remainder = digits % 10
    if remainder == 0:
        return countZeros(digits//10, count + 1)
    return countZeros(digits//10, count)

""" COUNT STEPS """
def countSteps(num):
    return helper(num, 0)
def helper(num, steps):
    if num == 0:
        return steps
    if (num % 2 == 0):
        return helper(num //2, steps+1)
    return helper(num-1, steps+1)


print(countSteps(41))
