#insertion of elements using queue
'''from queue import Queue
q=Queue()
n=int(input("Enter the number of elements:"))
for i in range(n):
    val=int(input("enter the value:"))
    q.put(val)
print("Queue elements:")
for i in range(q.qsize()):
    val=q.get()
    print(val,end="")
    q.put(val)'''

#delete of elements using queue/queue empty
'''from queue import Queue
q=Queue()
n=int(input("Enter the number of elements:"))
for i in range(n):
    val=int(input("enter the value:"))
    q.put(val)
while not q.empty():
    print(q.get(),"deleted")
print("Queue empty")'''

#insert elements in fixed queue
'''from queue import Queue
q=Queue(3)
n=int(input("Enter the number of elements:"))
for i in range(n):
    val=int(input("enter the value:"))
    if not q.full():
        q.put(val)
    else:
        print("Queue is full")
if q.full():
    print("Queue is full")
print("Queue",list(q.queue))'''

#collections in queue
#1.counter
#2.defaultdict
#3.OrderedDict
#4.deque
#5.namedtuple
#6.ChainMap
#7.UserDict
#8.UserList
#9.UserString

#counter
'''from collections import Counter
nums=input("enter text or number:").split()
c=Counter(nums)
print("counter:",c)'''

'''from collections import Counter
nums=input("enter text or number:").split()
c=Counter(nums)
print("counter:",c)
print("most common",c.most_common(2))'''

#default dict
'''from collections import defaultdict
d=defaultdict(int)
n=int(input("enter no of elements:"))
for i in range(n):
    val=input("enter the value:")
    d[val]+=1
print("dictonary:",dict(d))'''

#ordered dictionary
'''from collections import OrderedDict
d=OrderedDict()
n=int(input("enter no of elements:"))
for i in range(n):
    key=input("Enter the key:")
    val=input("enter the value:")
    d[key]=val
print("Ordered Dictionary:",d)'''

#namedtuple
'''from collections import namedtuple
student=namedtuple("student",["name","age","marks"])
name=input("enter the name:")
age=int(input("enter the age:"))
marks=int(input("enter the marks"))
s=student(name,age,marks)
print("Students:",s)
print("Marks:",s.marks)
print("Age:",s.age)'''

#chainmap
'''from collections import ChainMap
d1={}
d2={}
n=int(input("enter the number of elements in d1:"))
for i in range(n):
    key=input("enter the key:")
    val=input("enter the value:")
    d1[key]=val
n=int(input("enter no of elements:"))
for i in range(n):
    key=input("Enter the key:")
    val=input("enter the value:")
    d2[key]=val
c=ChainMap (d1,d2)   
print("First Dictionary:",d1)
print("second Dictionary:",d2)
print("ChainMap:",c)'''

#UserDict & UserList
'''from collections import UserDict,UserList
class MyDict(UserDict):
    def add_data(self,key,value):
        self.data[key]=value
d=MyDict()
n=int(input("enter no of elements:"))
for i in range(n):
    key=input("Enter the key:")
    value=input("enter the value:")
    d.add_data(key,value)
print("Dictionary:",d)

class MyList(UserList):
    def add_element(self,value):
        self.data.append(value)
l=MyList()
numbers=input("enter the numbers:").split()
for i in numbers:
    l.add_element(i)
print("List:",l) '''   

#user string
'''from collections import UserString
s=UserString(input("enter the string:"))
x=input("enter the prefix:")
y=input("enter the suffix:")
print("Starts with:",s.startswith(x))
print("Ends with:",s.endswith(y))'''

#deque operations
#insert-append() ,appendleft()
'''from collections import deque
d=deque(map(int,input("enter elements:").split()))
val=int(input("enter the value to append:"))
d.append(val)
print("Deque:",d)
val=int(input("enter the value to append left:"))
d.appendleft(val)
print("Deque:",d)'''

#delete-pop(),popleft() 
'''from collections import deque
d=deque(map(int,input("enter elements:").split()))
val=int(input("enter the value to append:"))
d.append(val)
print("Deque:",d)
val=int(input("enter the value to append left:"))
d.appendleft(val)
print("Deque:",d)
x=d.pop()
print("deleted element:",x)
print("deque:",d)
y=d.popleft()
print("deleted element:",y)
print("deque:",d)'''

#add elements-extend(),extendleft()
'''from collections import deque
d=deque(map(int,input("enter the elements:").split()))
x=list(map(int,input("enter the elements to add:").split()))
d.extend(x)
print("Deque",d)
y=list(map(int,input("enter the elements to add left:").split()))
d.extendleft(y)
print("Deque",d)'''       
       
#remove(),reverse()
'''from collections import deque
d=deque(map(int,input("enter the elements:").split()))
val=int(input("enter the value to remove:"))
print("Deque:",d)
d.remove(val)
print("Deque:",d)
d.reverse()
print("Reversed deque:",d)'''

#rotate()
'''from collections import deque
d=deque(map(int,input("enter the elements:").split()))
r=int(input("enter the value to rotate:"))#default -anticlockwise
print("Deque:",d)
d.rotate(r)
print("Deque:",d)
r=int(input("enter the value to rotate:"))
d.rotate(-r)#clockwise
print("Deque:",d)'''

#index(),copy(),clear()
'''from collections import deque
d=deque(map(int,input("enter the elements:").split()))
print("Deque:",d)
x=int(input("enter the value to search index:"))
print("index:",d.index(x))
pos=int(input("enter the position:"))
y=int(input("enter the value:"))
d.insert(pos,y)
print("Deque:",d)
c=d.copy()
print("duplicate deque:",c)
d.clear()
print("Deque:",d)'''




















         
