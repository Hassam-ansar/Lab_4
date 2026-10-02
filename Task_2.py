
# queue = []

# def push(value):
#     queue.append(value)


# def pop(queue):

#     if(len(queue) == 0):
#         print(f"Queue is empty.")

#     else:


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add to the back
        self.items.append(item)

    def dequeue(self):
        # Remove from the front
        return self.items.pop(0)


q = Queue()
# 1. Add items (Enqueue)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

# 2. Remove items (Dequeue)
print(q.dequeue())  # Output: A
print(q.dequeue())  # Output: B
