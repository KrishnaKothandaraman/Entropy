from src.entropy_node import Node
from typing import List, Optional

# First in First Out
class EntropyQueue:
    def __init__(self):
        self.items: List[Node] = []
        self.head: Node = None
        self.tail: Node = None

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.printQueue()

    def dequeue(self) -> Optional[Node]:
        return_node = None
        if not self.head:
            return_node = None
        
        elif self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return_node = old_head
        else:
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return_node = old_head
        self.printQueue()
        return return_node

    def printQueue(self):
        cur_head = self.head
        if not cur_head:
            print("None")
        while cur_head:
            if cur_head == self.head == self.tail:
                print(f"None <- {cur_head.value} -> None")
            elif cur_head == self.head:
                print(f"None <- {cur_head.value} <-> ", end = "")
            elif cur_head == self.tail:
                print(f"{cur_head.value} -> None")
            else:
                print(f"{cur_head.value} <-> ", end="")
            cur_head = cur_head.next

    


