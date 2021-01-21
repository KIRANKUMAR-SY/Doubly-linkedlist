# Doubly-linkedlist
#Doubly linked list - append and prepend

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
