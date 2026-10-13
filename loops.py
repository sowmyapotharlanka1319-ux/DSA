#DATA STRUCTURES
#Loops
#sum of digits in a number
'''n=int(input("enter a number:"))
s=0
while n!=0:
    d=n%10
    s+=d
    n//=10
print("sum:",s)'''    

#reverse a given number
'''n=int(input("enter a number:"))
r=0
while n!=0:
    d=n%10
    r=r*10+d
    n//=10
print("reverse:",r)
#m-2
n=int(input("enter a number:"))
while n!=0:
    d=n%10
    n//=10
    print(d,end=" ")'''

#generate a even number
'''n=int(input("enter n:"))
i=1
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i+=1 '''

#generate odd natural numbers
'''n=int(input("enter n:"))
for i in range(1,n+1):
    if i%2==1:
        print(i,end=" ")'''

#2-D data
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()'''

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(i,end=' ')
    print()'''

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(j,end=' ')
    print()'''

#Hollow sqaure
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#hollow square pattern with diagnols
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1: #j=n-1-i(we can take this too)
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#hollow and daignol
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#hollow with +
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#diagnol and +
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#right angle triangle
'''n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()'''   

#reverse traingle
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() '''   

#inverted right triangle
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''        

#inverted reverse triangle
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() '''       


#Time cpmplexity and space complexity:
#In Data Structures and Algorithms (DSA), time and space complexity are the primary metrics
#used to measure the efficiency and scalability of an algorithm.

#Time complexity->It is the rate at which the execution time of an algorithm increases relative to the input size.
#Space complexity->Space complexity is the total amount of memory space required by a program to run to completion.

#O(n) is the constant time complexity & space complexity=O(1)
'''n=int(input("Enter a number:"))
print(n+100)'''

#O(n) is the5
#linear time complexity & space complexity =O(1) 
'''n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i,end=" ")'''

#O(n)-linear time complexity & space complexity=O(n)    
'''n=int(input("Enter a number:"))
arr=[]
for i in range(n):
    num=int(input("enter num:"))
    arr.append(num)
print("List",arr)'''    

#O(n^2)-TC, SC=O(1)
'''n=int(input("enter n:"))
num=1
for i in range(n):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()'''

#logarthmic TC=O(log(n)) ,SC=O(1)
'''n=int(input("Enter a value:"))
while n>1:
    print(n)
    n//=2
print(1)'''

#TC=O(n log(n)) SC=O( )
'''n=int(input("Enter a value:"))
for i in range(n):
    j=n
    while j>1:
        j//=2
        print("done")'''

'''n=int(input("Enter a value:"))
for i in range(n):
    j=n
    while j>1:
        j//=2
        print(j)'''

def count(n):
    if n==0:
        return 1
    return count(n-1)+count(n-1)
n=int(input("enter a number:"))
print("result:",count(n))























































