#print array
arr=[23,54,31,22,90,54,70]

#ex1:print array
for i in arr:
    print(i)

#ex2 : sum of all elements
total=0
for i in arr:
    total+=i

print("sum :",total)


#ex3 find largest
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("largest:",largest)

# ex4 find smallest
smallest =arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print("smallest",smallest)

# ex 5 count even and odd
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even",even)
print("odd",odd)

#ex6 reverse array
print (arr[::-1])

#ex7 find num in array
num=int(input("enter number"))
if num in arr:
    print("found")
else:
    print("not found")

#ex 7 count occurence
arr1 = [1, 2, 2, 3, 2, 4]

num1 = int(input("Enter number: "))
count =0
for i in arr1:
    if i==num1 :
        count +=1
print("occurence",count)
#ex8
print("Maximum =", max(arr))
print("Minimum =", min(arr))

#ex9
arr2= arr+arr1
print(arr2)

#ex 10
arr3 = [10, 50, 30, 20, 40]

arr3.sort()

print("Second Largest =", arr3[-2])


#ex 11 remove duplicates
new_arr=[

]

for i in arr1:
    if i not in new_arr:
        new_arr.append(i)
print(new_arr)

#ex 12
arr = [10, 20, 30, 40, 50, 60]
for i in range(0, len(arr), 2):
    print(arr[i])

#ex13
arr = [10, 20, 30, 40, 50]
avg = sum(arr) / len(arr)
print("Average ", avg)
