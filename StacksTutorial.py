#Normal stack implementation
stack = []

#Push
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
print("Stack: ", stack)

#Pop
element= stack.pop()
print("Pop: ", element)

#Peek
topElement= stack[-1]
print("Peek: ", topElement)

#isEmpty
isEmpty= not bool (stack)
print("isEmpty:", isEmpty)

#Size
print("Size: ", len(stack))


#Class data structure for stacks
class Stack:
    def __init__(self):
        self.stack= []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

hisStack= Stack()

hisStack.push('A')
hisStack.push('B')
hisStack.push('C')
hisStack.push('D')
hisStack.push('E')

print("Stack: ", hisStack.stack)
print("Pop: ", hisStack.pop())
print("Peek: ", hisStack.peek())
print("isEmpty: ", hisStack.isEmpty())
print("Size: ", hisStack.size())


#Stacks implementation using linked lists
class Node:
    def __init__(self, value):
        self.value= value
        self.next= None

class Stack:
    def __init__(self):
        self.head= None
        self.size= 0

    def push(self, value):
        new_node= Node(value)
        if self.head:
            new_node.next= self.head
        self.head= new_node
        self.size += 1

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node= self.head
        self.head= self.head.next
        self.size -= 1
        return popped_node.value
    
    def stackSize(self):
        return self.size
    

mystack= Stack()
mystack.push('X')
mystack.push('Y')
mystack.push('Z')
mystack.push('P')
mystack.push('R')
print("Pop", mystack.pop())
print("Peek: ", mystack.peek())
print("isEmpty: ", mystack.isEmpty())
print("Size: ", mystack.size)