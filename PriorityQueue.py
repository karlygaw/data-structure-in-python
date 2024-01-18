class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        # Предполагается, что приоритет представляет собой числовое значение.
        element = (item, priority)
        self.queue.append(element)
        self.queue.sort(key=lambda x: x[1], reverse=True)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty")
        return self.queue.pop(0)[0]

    def peek(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty")
        return self.queue[0][0]

    def display(self):
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            print("Priority Queue:")
            for item, priority in self.queue:
                print(f"Item: {item}, Priority: {priority}")

priority_queue = PriorityQueue()

priority_queue.enqueue("Task 1", 3)
priority_queue.enqueue("Task 2", 1)
priority_queue.enqueue("Task 3", 2)

priority_queue.display()

print("Dequeue:", priority_queue.dequeue())
priority_queue.display()

print("Peek:", priority_queue.peek())
