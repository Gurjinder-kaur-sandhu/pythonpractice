# ex1:Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
items =list(map(int,input("enter numbers").split()))
unique_items=[]
 
for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("unique list",unique_items )

#ex2:Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
def check_firstlast(numbers):
    if numbers[0]==numbers[-1]:
        return True
    else:
        return False

numbers =list(map(int,input("enter numbers").split()))
print(check_firstlast(numbers))

#ex3 Iterate through a given list of numbers and print only those numbers which are divisible by 5
def divisible_by_5(nums):
    for num in nums:
        if num % 5 == 0:
            print(num)
nums=[5,77,20,15]
divisible_by_5(nums)


#ex4 Write a program to find how many times the substring “Emma” appears in a given string
s1 ="Emma is good developer. Emma is also a writer. Emma likes Python."
count = s1.count("Emma")
print("emma appeared",count,"times")

#ex5 Print the following pattern where each row contains a number repeated a specific number of times based on its value
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print( )

#ex 6:Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
palindrome=int(input("enter value of palindrone number"))
original= palindrome
reverse =0
while palindrome>0:
    digit=palindrome%10
    reverse=reverse * 10 + digit 
    palindrome =palindrome //10
if original == reverse:
    print("it is palindrome")
else:
    print("not a palindrome")

# ex 7:Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

def merge_list(lista,listb):
    final_list=[]
    for num in lista:
        if num %2!=0:
            final_list.append(num)
    for num in listb:
        if num %2==0:
            final_list.append(num)
    return final_list
lista=[98,65,43,22,49]
listb=[90,54,32,13,57]
print("final list is", merge_list(lista,listb))


#arr :without sort func bubble sort
arr=[43,23,12,12,56,22,45]
for i in range(len(arr)):
    for j in range(len(arr)-1-i): #-1 to avoid unnecessary check
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)