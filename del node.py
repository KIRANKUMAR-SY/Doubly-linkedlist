#!/usr/bin/env python
# coding: utf-8

# In[20]:


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
        
    def delnode(self,key):
        cur=self.head
        while cur:
            if cur.data==key and cur==self.head:
                if not cur.next:
                    cur=None
                    self.head=None
                    return
                
                #case 2
                else:
                    nxt=cur.next
                    cur.next=None
                    nxt.prev=None
                    cur=None
                    self.head=nxt
                    return
                    
            elif cur.data==key:
                #case 3
                if cur.next:
                    nxt=cur.next
                    pre=cur.prev
                    nxt.prev=pre
                    pre.next=nxt
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                    
                #case 4
                else:
                    pre=cur.prev
                    pre.next=None
                    cur.prev=None
                    cur=None
                    return
                
            cur=cur.next
            
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

dlist.delnode(1)
dlist.Printlist()


# In[18]:


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




