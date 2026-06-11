# 1 integer digit extraction and reversal
number=7536
while number > 0:
   digit= number%10
   number=number//10
   print(digit ,"\n")

# 2 Multi tiered income tax calculation
# first 10 k dollars -0%,next 20 k 10% and remaining income -20%
income=45000
tax_pay=0
print("given income",income,"\n")
if income<=10000:
   tax_pay=0
elif income<=20000:
   tax_pay=(income-10000)*10/100 
else:
   tax_pay= 0+(10000*10/100)#calculate tax between 10k and 20 k
   tax_pay +=(income-20000)*20/100 #remaining tax
print("total tax",tax_pay)


#ex3:nested loop for multiplication table 
for i in range(1,11):
    for j in range(1,11):
       print(i*j,end="\t")

    print("\n")
n=8
for i in range(n,n+1):
    for j in range(1,11):
       print(i*j,end="\t")

    print("\n")

# 4 half pyramid downwards
m=5
for h in range(m,0,-1):
    for l in range(h):
       print("*",end="")
    print()
    
# 5 custom Exponentiation Function
def exponent(base,exp):
    num=exp
    result=1
    while num>0:
        result=result*base
        num=num-1
    print(base,exp,result)
exponent(2,5)

#ex6 Check Palindrome Number
number=121
original=number
reverse=0
while number > 0:
   digit= number%10
   reverse=reverse*10+digit
   number=number//10
if original==reverse:
    print("number is palindrome")
else:
    print("not a palindrome")

#ex7 fibonacci series
num1,num2=0,1
print("fibonacci series")
for i in range(16):
   print(num1,end=" ")
   res=num1+num2
   num1=num2
   num2=res

#ex 8 check leap year
year=2021
if (year % 4 == 0 and year % 100 != 0):
   print("leap year")
elif (year % 400 == 0 and year %100 !=0):
   print("leap year")
else:
   print("not a leap year")

#ex9 merging 2 dictionaries

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

merge_dict=dict1|dict2
print(merge_dict)

#ex10 lists and find the elements that appear in both. Use Sets to perform the operation.
list1=[2,3,4]
list2=[4,8,9]
seta=set(list1)
setb=set(list2)

common=seta & setb
print(common)