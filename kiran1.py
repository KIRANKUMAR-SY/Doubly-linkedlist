#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def push(self,ndata):
        node=Node(ndata,self.head)
        node=self.head
        
    def Printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            if temp==self.head:
                return
            
    def sortedlist(self,nnode):
        cur=self.head
        
        if cur is None:
            nnode.next=nnode
            nnode=self.head
            
        elif cur.data>=nnode.data:
            while(cur.next!=self.head):
                cur=cur.next
            cur.next=nnode
            nnode.next=self.head
            self.head=nnode
            
        else:
            while(cur.next!=self.head and
                 cur.next.data<=nnode.data):
                cur=cur.next
                
            nnode.next=cur.next
            cur.next=nnode
            
arr = [12, 56, 2, 11, 1, 90]
 
list_size = len(arr)
 
# start with empty linked list
start = Linkedlist()
 
# Create linked list from the array arr[]
# Created linked list will be 1->2->11->12->56->90
for i in range(list_size):
    temp = Node(arr[i])
    start.sortedlist(temp)
 
start.Printlist()
            
        
        


# In[17]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
            
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        if self.head is None:
            node=Node(data)
            node.prev=None
            self.head=node
            
        else:
            node=Node(data)
            cur=self.head
            while(cur.next):
                cur=cur.next
            cur.next=node
            node.prev=cur
            node.next=None
            
    def prepend(self,data):
        if self.head is None:
            node=Node(data)
            node.prev=None
            self.head=node
            
        else:
            node=Node(data)
            self.head.prev=node
            node.next=self.head
            self.head=node
            node.prev=None
                        
    
    def Printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
dlist=DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.prepend(0)
dlist.Printlist()


        


# In[ ]:




