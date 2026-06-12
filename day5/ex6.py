""" ex1 Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid 
along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions
 rather than multiple loops, as a learning exercise."""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result=[[i,j,k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i + j + k != n
        
         ]
print(result)


"""ex2 Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space."""
n = int(input())
arr = list(map(int, input().split()))

arr = list(set(arr))  # remove duplicates
arr.sort()

print(arr[-2])

""" ex3 Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""

student=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    student.append([name, score])

grades = sorted(set(score for name, score in student))
second_lowest = grades[1]
names = []
for name, score in students:
    if score == second_lowest:
        names.append(name)
    for name in sorted(names):
        print(name)