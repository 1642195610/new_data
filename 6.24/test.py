from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional = None):
        self.data: Any = data
        self.next: Optional = next



    def __repr__(self):
        return f"Node({self.data})"


class LinkQueue:
    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None
        self.size = 0

    def put(self, item: Any) -> None:
        node: Node = Node(item)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            node: Node = self.front
            self.front = node.next
        self.size -= 1

    def is_empty(self) -> bool:
        return self.front is None

    def get(self,index) -> Any:
        if index < 0 or index > self.size:
            raise Exception("索引越界!!!")
        current = self.front
        t = 0
        dic = {}
        while current:
            dic ={t:current}
            if t == index:
                break
            t += 1
            current = current.next
        return dic[t]

    def __repr__(self):
        current = self.front
        str = ""
        while current:
            str += f"{current} <-- "
            current = current.next
        return str + "END"


if __name__ == '__main__':
    q = LinkQueue()
    q.put(111)
    q.put(222)
    q.put(333)
    q.put(444)
    print(q)
    q.pop()
    print(q)
    a = q.is_empty()
    print(a)
    print(q.get(0))
    print(q.get(2))
    print(q.get(1))
    print(q.size)


    