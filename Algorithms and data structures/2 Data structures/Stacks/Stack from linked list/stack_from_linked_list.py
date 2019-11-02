class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class Stack:

    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        top = self.top.next_node

        if top:
            self.top.next_node = top.next_node
            return top.value

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        new_node = Node(value)
        new_node.next_node = self.top.next_node
        self.top.next_node = new_node  
        


stack = Stack()
stack.push(12)
stack.push(7)
stack.push(6)
assert stack.pop() == 6
assert stack.pop() == 7
assert stack.pop() == 12

stack = Stack()
stack.push(7)
stack.push(6)
stack.push(2)
stack.push(1)
assert stack.pop() == 1
assert stack.pop() == 2
assert stack.pop() == 6
assert stack.pop() == 7
