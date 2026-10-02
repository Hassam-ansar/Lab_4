# # stack implementation using stack.

# stack = []

# for i in range(1,6):
#     stack.append(i)

# # Top element
# print(stack[0])

# # last element pop
# print(stack.pop())

# # Full stack display
# print(stack)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if(not self.is_empty()):
            return self.items.pop()
        return "Stack is empty!"

    # def top(self):
    #     if(not self.is_empty()):
    #         return self.items[-1]
    #     return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # def print_stack(self):
        
        

# 1. Create the stack
my_stack = Stack()

# 2. Push items onto it (bottom to top)
my_stack.push("Plate 1")
my_stack.push("Plate 2")
my_stack.push("Plate 3")

# my_stack.print_stack()


# print(my_stack.top())     # Output: Plate 3 (it's on top)
print(my_stack.pop())      # Output: Plate 3 (removed from the stack)
print(my_stack.size())     # Output: 2
print(my_stack.is_empty()) # Output: False
