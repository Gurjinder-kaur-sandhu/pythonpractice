# ex1:find dupicates
arr=[2,3,4,3,0,2,5,4,6,1,0,8,2]
duplicate=[]

for i in arr:
    if arr.count(i)>1 and i not in duplicate:
        duplicate.append(i)
print("duplicates",duplicate)

#ex2 calculating frequency of evry element
frequency={}#dict:store count and no both
    #dictionary.get(key, default_value) get function:If key exists → return its value.If key doesn't exist → return default value
for i in arr:
    frequency[i]=frequency.get(i,0)+1
print(frequency)

#ex3 moving all zeroes to end
arr1=[2,3,4,3,0,2,5,4,6,1,0,8,2]
result=[]
for i in arr1:
    if i !=0:
        result.append(i)
zeros=arr1.count(0)
for i in range (zeros):
    result.append(0)
print(result)


#ex4:find missing no 1 to n
arr2=[1,2,3,4,6]
n=6
#use formula for sum of natural numbers n*(n+1)//2
exp=n*(n+1)//2
actual=sum(arr2)
missing=exp-actual
print("missing number",exp-actual)

# ex5 find intersection:common
common=[]
for i in arr1:
    if i in arr2:
        common.append(i)
print(common)

#ex6 find union of two array
union=list(set(arr1+arr2)) #set store only unique values and then convert back to list

print(union)


#ex 7 rotate array left by one position
guri=[1,2,3,4,5]
first=guri[0]
for i in range(len(guri)-1):
    guri[i]=guri[i+1]
guri[-1]=first
print(guri)

#ex8 rotate array right by one position
arr = [1, 2, 3, 4, 5]
last = arr[-1]
for i in range(len(arr)-1, 0, -1): #(4start,0 stop,-1 step)4,3,2,1
    arr[i] = arr[i-1]
arr[0] = last
print(arr)

#ex9find pair with given sum
arr=[2,4,5,3,2]
target=7
for i in range(len(arr)): #outer loop:index
    for j in range(i+1,len(arr)):#all values of check for evry i :::+1 so that it avoid checking with sAMEN NO
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])

#ex10 separate even and odd no
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even",even)
print("odd",odd)