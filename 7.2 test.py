class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node{self.data}"

def pop(head,val):
    if head is None:
        raise Exception("为空!!!")
    else:
        f_false = Node(0)
        f_false.next = head
        curr = f_false
        while curr.next:
            if curr.next.data == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
    return f_false.next

def print_list(head):
    curr = head
    while curr:
        print("%s --> "%curr.data,end=" ")
        curr = curr.next

if __name__ == '__main__':
    j1 = Node(10)
    j2 = Node(20)
    j3 = Node(10)
    j4 = Node(40)
    j5 = Node(10)
    j1.next = j2
    j2.next = j3
    j3.next = j4
    j4.next = j5
    j5.next = None
    print(print_list(j1))
    a = pop(j1,10)
    print(print_list(a))