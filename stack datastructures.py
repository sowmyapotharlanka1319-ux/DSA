#stack-LIFO(Last In First Out)

#push operation
'''stack=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack.append(val)
print("Stack:",stack)
print("Peek:",stack[-1])
if len(stack)==0:
    print("stack is empty")
else:
    print("deleted element:",stack.pop())
print("Stack:",stack)
print("Peek:",stack[-1])'''

#push operation-delete all elements till stack empty
'''stack=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack.append(val)
print("Stack:",stack)
while len(stack)>0:
    print(stack.pop(),"deleted")
print("Stack empty",stack)'''

#push operation till overflow
'''stack=[]
size=int(input("enter the size:"))
n=int(input("enter the number of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    if len(stack)==size:
        print("Stack Overflow...")
    else:
        stack.append(val)
        print(val,"inserted")
print("Stack:",stack)'''

#push operation and merge 2 stacks
'''stack1=[]
stack2=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack1.append(val)
print("stack1:",stack1)
for i in range(n):
    val=int(input("enter a value:"))
    stack2.append(val)
print("stack2:",stack2)
stack1.extend(stack2)
stack1.sort()
print("Merged stack:",stack1)'''

#without using built-in functions
'''stack1=[]
stack2=[]
stack3=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack1.append(val)
print("stack1:",stack1)
for i in range(n):
    val=int(input("enter a value:"))
    stack2.append(val)
print("stack2:",stack2)

i,j=0,0
while i<len(stack1)and j<len(stack2):
    if stack1[i]<stack2[j]:
        stack3.append(stack1[i])
        i+=1
    else:
        stack3.append(stack2[j])
        j+=1
while i<len(stack1):
    stack3.append(stack1[i])
    i+=1
while j<len(stack2):
    stack3.append(stack2[j])
    j+=10
print("Merged stack:",stack3) '''   
    
#Implementation of stack expressions- Prefix
'''exp=input("enter a expression:")
stack=[]
result=""
def priority(op):
    if op=='^':
        return 3
    elif op in '*/':
        return 2
    elif op in '+-':
        return 1
    return 0
exp=exp[::1]
for ch in exp:
    if ch.isalnum():
        result+=ch
    else:
        while stack and priority(stack[-1])>priority(ch):
            result+=stack.pop()
        stack.append(ch)
while stack:
    result+=stack.pop()
print("prefix:",result[::-1])'''    
    
#postfix
'''exp=input("enter a expression:")
stack=[]
result=""
def priority(op):
    if op=='^':
        return 3
    elif op in '*/':
        return 2
    elif op in '+-':
        return 1
    return 0
for ch in exp:
    if ch.isalnum():
        result+=ch
    else:
        while stack and priority(stack[-1])>=priority(ch):
            result+=stack.pop()
        stack.append(ch)
while stack:
    result+=stack.pop()
print("postfix:",result)'''

#postfix --> prefix
'''exp=input("enter a expression:")
stack=[]
for ch in exp:
    if ch.isalnum():
        stack.append(ch)
    else:
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b+ch)
print("postfix:",stack[-1]) '''       
    















