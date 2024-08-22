from collections import deque

stack = deque()

stack.append("https://www.cnn.com/")
print(stack)
stack.append("https://www.cnn.com/world")
print(stack)
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

# Last In First Out(LIFO) This means that the last element added to the stack will be the first one to be removed. It's similar to a stack of plates where you can only add or remove plates from the top.