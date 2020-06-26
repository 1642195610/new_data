from typing import List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return f"({self.data})"

class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def get(self,index):
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr

    def insert(self,index,element):
        new_node= Node(element)
        if index <0 or index > self.size:
            raise Exception("索引越界")
        elif self.size ==0:
            self.head=new_node
            self.tail=new_node
        elif index ==1:
            new_node.next=self.head
            self.head=new_node
        elif index==self.size:
            self.tail.next=new_node
            self.tail=new_node
        else:
            prev=self.get(index-1)
            new_node.next=prev.next
            prev.next=new_node
        self.size +=1
    def __repr__(self):
        curr=self.head
        string=""
        while curr:
            string=string+f"{curr}-->"
            curr=curr.next
        return string +'END'

if __name__=='__main__':
    l=LinkList()
    l.insert(0,1)
    l.insert(1,2)
    l.insert(2,3)
    l.insert(1,4)
    print(l)