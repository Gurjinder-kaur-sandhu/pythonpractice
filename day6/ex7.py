""" ex1 In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
"""
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count

string = input().strip()
sub_string = input().strip()

print(count_substring(string, sub_string))

"""ex2"""
s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))

"""ex3 In Python, a string of text can be aligned left, right and center.

.ljust(width)

This method returns a left aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  """
# Enter your code here. Read input from STDIN. Print output to STDOUT
thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)
          + c
          + (c*(thickness-i-1)).ljust(thickness))
          .rjust(thickness*6))
    
"""ex4 You are given a string  and width .
Your task is to wrap the string into a paragraph of width ."""
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)


"""ex5 Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters."""
N, M = map(int, input().split())

# Top half
for i in range(1, N, 2):
    pattern = '.|.' * i
    print(pattern.center(M, '-'))

# Middle
print('WELCOME'.center(M, '-'))

# Bottom half
for i in range(N-2, 0, -2):
    pattern = '.|.' * i
    print(pattern.center(M, '-'))
 

"""ex6 Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary"""

def print_formatted(number):
    # your code goes here

    width = len(bin(number)) - 2

    for i in range(1, number + 1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(dec.rjust(width),
              octal.rjust(width),
              hexa.rjust(width),
              binary.rjust(width))