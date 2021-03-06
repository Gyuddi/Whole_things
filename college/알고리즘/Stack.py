from Node_structure import Node
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,item):
        self.top = Node(item,self.top)
        self.size += 1

    def peek(self):
        if self.size != 0:
            return self.top.item
    
    def pop(self):
        if self.size != 0:
            top_item = self.top.item
            self.top = self.top.next
            self.size -= 1
            return top_item
    
    def print_stack(self):
        print("top -> \t", end="")
        p = self.top
        while p:
            if p.next != None:
                print(p.item,"->",end="")
            else:
                print(p.item,end="")
            p = p.next
        print()

# s = Stack()
# s.push("apple")
# s.push("orange")
# s.push("banana")
# s.pop()
# s.print_stack()
