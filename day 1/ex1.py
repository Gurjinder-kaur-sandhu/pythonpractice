#exercise 1: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum
def  cal_product(a,b):
    product=a*b
    if product<=1000:
        print(product)
    else:
        print(a+b)

n1=int(input("enter first no"))
n2=int(input("enter second no"))

cal_product(n1,n2)


#exercise 2: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
prev_no=0
for cur_no in range(10):
    total=cur_no + prev_no
    print("current no",cur_no,
          "previous no",prev_no,
          "sum",total)
    prev_no=cur_no 
     

#exercise 3:Display only those characters which are present at an even index number in given string.
str1=input("enter string")
for i in range(len(str1)):
    if i%2==0:
        print(str1[i]) 

#exercise 4: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

def remove_characters(s,n):
    return s[n:]
str2=input("enter string")
n=int(input("enter val of n"))
print("string is",remove_characters (str2 ,n))

#exercise 5: Variable Swapping (The In-Place Method) Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable
a=9
b=8
a,b=b,a #tuple unpacking
print("value of a",a)
print("value of b",b)

#exercise 6:Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
n3=int(input("enter no"))
fact=1
for i in range(1,n3+1):
    fact=fact*i
print("factorial of",n3,"is",fact)

#exercise 7
fruits=["apple","mango","kiwi","grapes","pineapple"]
fruits.append("orange") #take one


fruits.pop(1)
print(fruits)

# exercise 8 Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
str4="python"
print(str4[::-1]) 

# exercise 9  Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
sentence="gurisandhu"
count =0
for ch in sentence:
    if ch in "aeiou":
        count += 1
print(count)

#exercise 10  Given a list of integers, find and print both the largest and the smallest numbers.
numbers=[4,56,3,2,11,33,99]
largest= max(numbers)
smallest = min(numbers)
print("largest and smallest number is",largest," ",smallest)