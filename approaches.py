 #strong number
'''while True:
    n=int(input())
    copy=n
    s=0
    while n!=0:
        d=n%10
        f=1
        i=1
        while i<=d: #for i in range(1,d+1)
           f*=i
           i+=1
        s+=f
        n//=10
    if s==copy:
        print("is a strong number",copy)
    else:
        print("is not a strong number",copy)'''

#1/2!+2/3!+3/4!+...n
'''n=int(input("Enter n:"))
total=0
fact=1
for i in range(1,n+1)
    fact*=i+1
    sum+=i/fact
print(sum)'''

#naive approach
'''arr=list(map(int,input("Enter elements:").split())
value=int(input("Enter value:"))
count=0
for i in arr:
         if i==value:
             count+=1
print(value,"occurences are:",count)'''

#bruteforce approach-find the possibilities
'''arr=list(map(int,input("Enter a elements:").split()))
target=int(input("enter a value:"))
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
         if  arr[i]+arr[j]==target:
             print(arr[i],arr[j])'''

#examples
#find maximum element
'''arr=list(map(int,input("Enter a elements:").split()))
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)''' #21 32 44 56  o/p:56

#Check whether a string is a palindrome
#Problem: Check whether a string reads the same forward and backward
'''while True:
    s =input("enter the string:")#madam-palindrome,data-not palindrome
    found = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            found = False
            break
    print("Palindrome"if found else "Not Palindrome")'''
       
#greedy approach->A greedy algorithm makes the best possible local choice
#at each step, hoping it leads to a global optimum.
'''coins=list(map(int,input("enter the coins:").split()))
amount=int(input("enter amount:"))
total_count=0
for coin in coins:
    count=amount//coin
    if count>0:
        print(coin,"rupees:",count)
        total_count+=count
        amount%=coin
print("Total coins:",total_count)'''

#BackTracking-->Backtracking is a systematic trial-and-error technique that builds a
#solution incrementally and undoes ("backtracks") choices when a path leads to a dead end.
'''n=int(input("enter n:"))#2
def backtrack(s):
    if len(s)==n:
        print(s)
        return
    backtrack(s+"0")
    backtrack(s+"1")
backtrack("") #00 01 10 11'''

#tail recursion in back tracking
'''def num(n):#5
    if n==0:
        return
    num(n-1)
    print(n,end=' ')
n=int(input("Enter n:"))
num(n) #12345'''

#Nested recursion
'''def fun(n): #5
    if n>10:
        return n
    return (fun(fun(n+2)))#f(f(5+2))
n=int(input("Enter n:"))
print(fun(n))#11'''

#summate the values in an array
'''arr=list(map(int,input("Enter the elements:").split()))
total=0
for val in arr:
    total+=val
print("Sum:",total)'''

#max value in an array
'''arr=list(map(int,input("Enter a elements:").split()))
max=arr[0]
for val in arr:
    if val>max:
        max=val
print("largest value",max)'''

#min value in an array
'''arr=list(map(int,input("Enter a elements:").split()))
max=arr[0]
for val in arr:
    if val < max:
        max=val
print("smallest value",max)'''

#reverse an array
'''arr=list(map(int,input("Enter elements:").split()))
for val in range(len(arr)-1,-1,-1): #[start,stop,step]
    print(arr[val],end=' ')'''

#remove duplicates in an array
'''arr=list(map(int,input("Enter the elements:").split()))
result=[]
for val in arr:
    if val not in result:
        result.append(val)
print(*result)'''

#print count of even and odd num in an array
'''arr=list(map(int,input("enter the elements:").split()))
even=0
odd=0
for val in arr:
    if val%2==0:
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd:",odd)'''

#rotate an array clockwise direction
'''arr=list(map(int,input("Enter the elements:").split()))
k=int(input("Enter rotation:"))
k%=len(arr)
arr=arr[k:]+arr[:k]
print(*arr)'''         
        
#anti clockwise
'''arr=list(map(int,input("Enter the elements:").split()))
k=int(input("Enter rotation:"))
k%=len(arr)
arr=arr[-k:]+arr[:-k]
print(*arr)'''         

#Searching in Arrays 1D/2D        
#search an element and return its index value in a 1-D array
'''arr=list(map(int,input("Enter the values:").split()))
search=int(input("Enter the element to be searched"))
found=False
for i in range(len(arr)):
         if arr[i]==search:
             print("element found at:",i)
             found= True
             break
if not found:
    print("element out of range:")'''

#In 2D array
'''n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
search=int(input("enter the element to be searched:"))    
found=False
for i in range(n):
    for j in range(n):
        if arr[i][j]==search:
            print("element found at row:",i,"col",j)
            found=True
            break
if not found:
    print(" element out of  range")'''

#Total
'''n=int(input("enter the size:"))
s=0
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
   for j in range(n):
        s+=arr[i][j]
print("Total:",s)'''

# Adding row-wise & col-wise
'''n=int(input("enter the size:"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    s=0
    for j in range(n):
        s+=arr[i][j]
    print("Row:"i+1,"sum:",s)
print()
for j in range(n):
    s=0
    for j in range (n):
        s+=arr[i][j]
    print("Col:",j+1,"sum:",s)'''    
    
#Adding diagnol & Anti-diagnol
'''n=int(input("enter the size"))
arr=[]
di=0
ad=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
           di+=arr[i][j]
        if i+j==n-1:
            ad+=arr[i][j]
print("Diagnol sum:",di)
print("Anti-Diagnol sum:",ad)'''


#types of searchs:
'''1.Linear
2.Binary
3.Jump Search'''

#Binary Search
'''arr=list(map(int,input("Enter the values:").split()))
arr.sort()
val=int(input("enter a element to search:"))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==val:
        print("element found at mid",mid)
        break
    elif arr[mid]<val:
        low=mid+1
    else:
        high=mid-1
else:
    print("element not found")'''

#find the square root of a number using binar search pattern
'''val=int(input("enter the element:"))
low=0
high=val
while low<=high:
    mid=(low+high)//2
    if mid*mid==val:
        print("square root:",mid)
        break
    elif mid*mid<val:
        low=mid+1
    else:
        high=mid-1
else:
    print("integer square root",high)'''

#sorting
'''1.Bubble sort
2.Selection sort
3.Insertion
4.Radix
5.Merge
6.Quick'''

#Bubble sort
'''arr=list(map(int,input("enter the elements:").split()))
n=len(arr)-1
for i in range(n):
    for j in range (n-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)'''

#selection sort
'''arr=list(map(int,input("enter the elements:").split()))
n=len(arr)
for i in range(n):
    minindex=i
    for j in range(i+1,n):
        if arr[j] < arr[minindex]:
            minindex=j
    arr[i],arr[minindex]=arr[minindex],arr[i]
print(*arr)'''

#Insertion sorting
'''arr=list(map(int,input("enter the elements").split()))
n=len(arr)
for i in range(n):
    x=arr[i]
    j=i-1
    while j>=0 and arr[j]>x:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=x
print(*arr)'''

#divide & conquer
'''1.merge sort
2.Quick sort'''
    
#merge sort
'''def mergesort(arr):
    if len(arr)<=1: 
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    result=[]
    while left and right:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result+left+right
arr=list(map(int,input("enter the elements:").split()))
print(mergesort(arr))'''

#highest flip/total flip
'''def pancakesort(arr):
    n=len(arr)
    for size in range(n,1,-1):
        max_index=arr.index(max(arr[:size]))
        arr[:max_index+1]=arr[:max_index+1][::-1]
        arr[:size]=arr[:size][::-1]
    return arr
arr=list(map(int,input("enter the element:").split()))
print("sorted array:",pancakesort(arr))'''

#quick sort
'''def quicksort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[-1]#right side(end)
    left=[x for x in arr[:-1]if x<=pivot]
    right=[x for x in arr[:-1]if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)
arr=list(map(int,input("enter elements:").split()))
print("Sorted array:",quicksort(arr))'''

#Traversals of an array
#patterns of an array
'''n=int(input("Enter the size of matrix:"))
arr=[[0]*n for _ in range(n)]
print(arr)
top=0
bottom=n-1
left=0
right=n-1
num=1
while top<=bottom and left<=right:
    #top,from left to right
    for i in range(left,right+1):
        arr[top][i]=num
        num+=1
    top+=1
    #right,from top to bottom
    for i in range(top,bottom+1):
        arr[i][right]=num
        num+=1
    right-=1
    #bottom,from right to left
    for i in range(right,left-1,-1):
        arr[bottom][i]=num
        num+=1
    bottom-=1
    #left,from bottom to top
    for i in range(bottom,top-1,-1):
        arr[i][left]=num
        num+=1
    left+=1
for row in arr:
    for x in row:
        print(f"{x:4}",end='')
    print()'''


#clockwise(spiral)
'''while True:
    n=int(input("enter matrix size: "))
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input("enter numbers: ").split())))
    top=0
    bottom=n-1
    left=0
    right=n-1
    num=1
    while top<=bottom and left<=right:
        #top from bottom to right
        for i in range(left,right+1):
            print(arr[top][i],end=" ")
            num+=1
        top+=1
        #right from top to bottom
        for i in range(top,bottom+1):
            print(arr[i][right],end=" ")
        right-=1
        #bottom from right to left
        for i in range(right,left-1,-1):
            print(arr[bottom][i],end=" ")
        bottom-=1
        #left from bottom to top
        for i in range(bottom,top-1,-1):
            print(arr[i][left],end=" ")
        left+=1'''

#second largest
'''arr=list(map(int,input("Enter elements:").split()))
if len(arr)<2:
    print("Not enough elements")
else:
    largest=float('-inf')
    second=float('-inf')
    for val in arr:
        if val>largest:
            second=largest
            largest=val
        elif val>second and val!=largest:
            second=val
    if second==float('-inf'):
        print("No second value exists")
    else:
        print("Second Largest",second)'''

#Tom Riddles Anagram
'''str1=input("enter:")
str2=input("enter:")
str1.replace(" ","")
str2.replace(" ","")
if len(str1)==len(str2):
    str1.upper()
    str2.upper()
    if sorted(str1)== sorted(str2):
        print("The data is Anagram")
    else:
        print("not Angaram")
else:
    print("Not")'''

#m-2
'''s1=input("enter first string:").lower().replace(' ','')
s2=input("enter second string:").lower.replace(' ','')
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Tom Riddles Anagram")
    else:
        print("Not")
else:
    print("Not")'''

#multiple testcases
'''while True:
    s1=input("enter first string:").lower().replace(' ','')
    s2=input("enter second string:").lower().replace(' ','')
    s1=''.join(ch for ch in s1 if ch.isalpha())
    s2=''.join(ch for ch in s2 if ch.isalpha())
    if len(s1)==0 or len(s2)==0:
        print("Not Tom Riddles Anagram")
    elif len(s1)==1 or len(s2)==1:
        print("Not Tom Riddles Anagram")
    elif len(s1)!=len(s2):
        print("Not Tom Riddles Anagram")
    elif len(set(s1))== 1 and len(set(s2))==1:
        print("Not Tom Riddles Anagram")
    elif sorted(s1)==sorted(s2):
            print("Tom Riddles Anagram")
    else:
        print("Not")'''

#robustness ->ability of an algorithm or data structure to handle errors, unexpected inputs,
#and adverse conditions gracefully without crashing or producing incorrect results.
'''arr=[11,22,33,44]
index=int(input("Enter the index:"))
if 0<=index<len(arr):
    print(arr[index])
else:
    print("Invalid index")'''

#search element in a rotated array
'''arr=list(map(int,input("enter the elements: ").split()))
search=int(input("enter a value to be searched:"))
low=0
high=len(arr)-1
ans=-1
while low<high:
    mid=(low+high)//2
    if arr[mid]==search:
        ans=mid
        break
    if arr[low]<=arr[mid]:
        if arr[low]<=search<=arr[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if arr[mid]<=search<=arr[high]:
            low=mid+1
        else:
            high=mid-1
print(ans) '''

#finding the first occurence of a number
'''arr=list(map(int,input("enter the elements:").split()))
num=int(input("enter the value to be searched:"))
low=0
high=len(arr)-1
ans=-1
while low <=high:
    mid=(low+high)//2
    if arr[mid]==num:
        ans=mid
        high=mid-1
    elif arr[mid]<=num:
        low=mid+1
    else:
        high=mid-1
print("lowest occurence index:",ans)'''        

#finding last occurence of a number    
'''arr=list(map(int,input("enter the elements:").split()))
num=int(input("enter the value to be searched:"))
low=0
high=len(arr)-1
ans=-1
while low <=high:
    mid=(low+high)//2
    if arr[mid]==num:
        ans=mid
        low=mid+1
    elif arr[mid]<num:
        low=mid+1
    else:
        high=mid-1
print("highest occurence index:",ans) '''    
        
#finding the count of occurence of a number
arr=list(map(int,input("enter the elements:").split()))
num=int(input("enter the value to be searched:"))
low=0
high=len(arr)-1
first,last=-1,-1
# Finding first occurrence
while low<=high:
    mid=(low+high)//2
    if arr[mid]>=num:
        if arr[mid]==num:
            first=mid
        high=mid-1
    else:
        low=mid+1
# Finding last occurrence
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]<=num:
        if arr[mid]==num:
            last=mid
        low=mid+1
    else:
        high=mid-1
# Finding count
print(last-first+1 if first!=-1 else 0)



























    
        
    
    
    
















    













































