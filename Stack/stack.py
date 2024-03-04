#creating stack using normal list

class Stack():
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        self.stack.reverse()
        values = [str(x) for x in self.stack]
        return '\n'.join(values)
    def isEmpty(self):
        if len(self.stack) ==0:
            return True
        else:return False
    def push(self,value):
        self.stack.append(value)
        return "The value is successfully pushed"
    def pop(self):
        if len(self.stack) == 0 : 
            return "The stack is empty"
        else:
            value = self.stack.pop(-1)
            return value

new_stack = Stack()

new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)
new_stack.push(6)
print(new_stack.pop())
#print(new_stack)