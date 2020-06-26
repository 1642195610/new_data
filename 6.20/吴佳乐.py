from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return f"Nade({self.data})"
class   LinkList:
    def  __init__(self):
        self.head=None
    def inaert_head(self,data):
        new_node=Node(data)
        if self.head:
           new_node.next=self.head
        self.head=new_node

    def peint_list(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def __repr__(self):
        current=self.head
        result=""
        while current:
          result +=f"{current}-->"
          current =current.next
          return result+"END"
    def append(self,data):
        if self.head is None:
            self.inaert_head(data)
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=Node(data)
    def insert(self,i,data):
        if self.head is None or i ==1:
            self.inaert_head(data)
        else:
            curr =self.head
            prev =self.head
            j =1
            while j<i:
                prev=curr
                curr=curr.next
                j+=1
            new_node=Node(data)
            prev.next=new_node
            new_node.next=curr
    def linklist(self,odj:List):
        new_node=Node(odj[0])
        self.head=new_node
        curr=self.head
        for i in odj[1:]:
            curr.next=Node(i)
            curr=curr.next
    def delete_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head=self.head.next
    def pop(self):
        curr=self.head
        if self.head is None:
            print("空链表")
        else:
             while curr.next.next:
                 curr=curr.next
             temp=curr.next.data
             curr.next=None
        return temp
    def delete_tail(self):
        curr=self.head
        prev=self.head
        while curr.next:
            prev=curr
            curr=curr.next
        else:
            temp=curr
            prev.next=None
        return temp
if __name__ == '__main__':
    j=LinkList()
    j.linklist([1,2,3,4,5])
    j.inaert_head(1)
    j.append(2)
    j.append(3)
    j.insert(2,100)
    j.peint_list()
    print(j)
    print("---------------")
    j.delete_head()
    print(j.pop())
    print(j.delete_tail())
    print(j)