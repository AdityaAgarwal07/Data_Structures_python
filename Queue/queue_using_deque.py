from collections import deque

queue = deque()

queue.appendleft(5)
queue.appendleft(8)
queue.appendleft(10)
print(queue)
queue.pop()
print(queue)

# A queue is FIFO (First In, First Out). This means that the first element added to the queue will be the first one to be removed. It's like a line of people waiting where the person who arrives first is served first.