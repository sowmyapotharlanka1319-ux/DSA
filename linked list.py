#single linkedlist insert from beginning
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("SLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#m-2
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode    
print("SLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#insert at end & delete at beginning
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode    
print("SLL:before delete ")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
#delete at beginning
if head is None:
    print("SLL empty....")
else:
    head=head.next
print("SLL:after delete")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#insert at beginning and delete at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("SLL:before delete")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
#delete at end
if head is None:
    print("SLL empty...")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
print("SLL:after delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#insert at position
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("SLL:before delete")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
pos=int(input("enter the position"))
data=int(input("enter the data"))
newnode=node(data)
if pos==1:
    newnode.next=head
    head=newnode
else:
    temp=head
    count=1
    while temp and count < pos-1:
        temp=temp.next
        count+=1
    if temp is None:
        print("Invalid position")
    else:
        newnode.next=temp.next
        temp.next=newnode
print("SLL:after insert:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#delete a value in SLL by position
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of node:"))
for i in range(n):
    data=int(input("enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("after insertion:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
pos=int(input("enter the position:"))
if pos<1 or head is None:
    print("invalid position:")
elif pos==1:
    head=head.next
else:
    temp=head
    count=1
    while temp.next and count<pos-1:
        temp=temp.next
        count+=1
    if temp.next is None:
        print("Invalid position:")
    else:
        temp.next=temp.next.next
print("After deletion:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#delete a value in SLL
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter no. of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("After insertion:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")
value=int(input("enter value to be deleted:"))
if head is None:
    print("SLL is empty:")
elif head.data==value:
    head=head.next
else:
    temp=head
    count=1
    while temp.next and temp.next.data!=value:
        temp=temp.next
    if temp.next is None:
        print("value no found")
    else:
        temp.next=temp.next.next
print("After deletion:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")'''

#reverse the SLL    
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter no. of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("After insertion:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")

prev=None
current=head
while current:
    nextnode=current.next
    current.next=prev
    prev=current
    current=nextnode
head=prev
print("Reversed SLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''   
    
#design a linkedlist
'''class node:
    def __init__(self,val):
        slef.val=val
        self.next=None
class MyLinkedList:
    def get(self,index:int)->int:
        current=self.head
        count=0
        while current:
            if count==index:
                return current.value
            current=current.next
            count+=1
        return -1
    def addAtHead(self,val:int)->None:'''
    
#double linkedlist
#insert at beginning
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter the no.of nodes:"))
for i in range(n):
    data=int(input("enter the value:"))
    newnode=node(data)
    newnode.next=head
    if head is not None:
        head.prev=newnode
    head=newnode
print('DLL')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('Tail') '''   

#insert at end        
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter the no.of nodes:"))
for i in range(n):
    data=int(input("enter the value:"))
    newnode=node(data)
    newnode.next=head
    if head is not None:
        head=newnode
        else:
            temp=head
            while temp.next:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
print("DLL")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('Tail')'''    

#Delete at beginning in DLL
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
n=int(input("enter no. of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Before deletion:")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")
if head is None:
    print("DLL is empty")
else:
    head=head.next
    if head:
        head.prev=None
print("After deleting at beginning:")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")'''

        
# Delete at end of DLL
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

head=None
n=int(input("enter no. of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Before deletion:")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")
# Delete at end
if head is None:
    print("DLL is empty")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next:
        temp=temp.next
    temp.prev.next=None
print("After deleting at end:")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")'''

#insert at a position
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter the no.of nodes:"))
for i in range(n):
    data=int(input("enter the value:"))
    newnode=node(data)
    newnode.next=head
    if head is not None:
        head.prev=newnode
    head=newnode
print('DLL')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('Tail') 
pos=int(input("enter the position:"))
val=int(input("enter the value:"))
newnode=node(val)
if pos<1:
    print("Invalid position")
elif pos==1:
    newnode.next=head
    if head:
        head.prev=newnode
    head=newnode
else:
    temp=head
    count=1
    while temp and count<pos-1:
        temp=temp.next
        count+=1
    if temp is None:
        print("Inavlid position")
    else:
        newnode.next=temp.next
        newnode.prev=temp
        if temp.next:
            temp.next.prev=newnode
        temp.next=newnode
print("After inserting at a position DLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#delete at a position in DLL
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter the no.of nodes:"))
for i in range(n):
    data=int(input("enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("DLL")
temp=head
while temp:
    print(temp.data,end='<->')
    temp=temp.next
print('Tail')
pos=int(input("enter the position:"))
# Delete at position
if pos<1 or head is None:
    print("Invalid position")
elif pos==1:
    head=head.next
    if head is not None:
        head.prev=None
else:
    temp=head
    count=1
    while temp and count<pos:
        temp=temp.next
        count+=1
    if temp is None:
        print("Invalid position")
    else:
        temp.prev.next=temp.next
        if temp.next is not None:
            temp.next.prev=temp.prev
print("After deletion:")
temp=head
while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("Tail")'''
        
#Delete a value in DLL
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter the no.of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("DLL:")
temp=head
while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("Tail")
value=int(input("Enter the value to be deleted:"))
# Delete a value
temp=head
while temp and temp.data!=value:
    temp=temp.next
if temp is None:
    print("Value not found")
elif temp==head:
    head=head.next
    if head:
        head.prev=None
else:
    temp.prev.next=temp.next
    if temp.next:
        temp.next.prev=temp.prev
print("After deletion:")
temp=head
while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("Tail")'''

#circular linked list create
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
        temp=head
    else:
        temp.next=newnode
        temp=newnode
if head is not None:
    temp.next=head
if head is None:
    print("SLL is empty:")
else:
    temp=head
    while True:
        print(temp.data,end="->")
        temp=temp.next
        if temp==head:
            break
    print("Back to the head")'''

#circular linked list create and traversal
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
        temp=head
    else:
        temp.next=newnode
        temp=newnode
if head is not None:
    temp.next=head
if head is None:
    print("SLL is empty:")
else:
    temp=head
    while True:
        print(temp.data,end="->")
        temp=temp.next
        if temp==head:
            break
    print("Back to the head")
start=int(input("Enter starting point:"))
temp=head
while temp and temp.data!=start:
    temp=temp.next
    if temp==head:
        break
if temp is None or temp.data!=start:
    print("Starting value not found")
else:
    print("Circular traversal:")
    start_node=temp
    while True:
        print(temp.data,end="->")
        temp=temp.next
        if temp==start_node:
            break
    print("Back to head")

            
    



