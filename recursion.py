#direct recursion-> happens when a function calls itself directly inside its own body. 
'''def numbers(n):
    if n==0:#base condition
        return
    print(n)
    numbers(n-1)#iterative cond
n=int(input("enter n:"))
numbers(n)'''

#factorial of a number(direct recursion)
'''def fact(n):
    if n==1:#base
        return 1
    return n*fact(n-1)#recursive
n=int(input("Enter n:"))
print("Factorial:",fact(n))'''

#indirect recursion
#indirect recursion (also called mutual recursion) happens when a function calls a
#second function,which then calls the first function back, forming a circular chain
'''def one(n):
    if n<=0:#base
        return
    print("one:",n)
    two(n-1)#iterative
def two(n):
    if n<=0:#base
        return
    print("two:",n)
    one(n-1)#iterative
n=int(input("enter a number:"))
one(n)'''

#even or odd(indirect recursion)
'''def even(n):
    if n==0:
        print(copy,"is even.")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print(copy,"is odd.")
        return
    even(n-1)
n=int(input("Enter a number:"))
copy=n
even(n)'''

#Tree Recursion-->The function calls itself once or multiple times per execution.
'''def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    fun(n-1)
n=int(input("enter the number:"))
fun(n)'''

#fibonaccci series
def fib(n):
    if n<=1:
        return n 
    return fib(n-1)+fib(n-2)
n=int(input("enter the number:"))
for i in range(n):
    print(fib(i),end=" ")
    

    

    























