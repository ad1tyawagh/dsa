import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)

# FIFO
while not q.empty():
    print(q.get())

s = queue.LifoQueue()

s.put(1)
s.put(2)
s.put(3)

# LIFO
while not s.empty():
    print(s.get())