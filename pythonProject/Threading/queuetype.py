import queue

q=queue.Queue()
q.put(400)
q.put(100)
q.put(50)
q.put(300)

while not q.empty():
    print(q.get(),end=' ')

print()

lq=queue.LifoQueue()
lq.put(400)
lq.put(100)
lq.put(50)
lq.put(300)

while not lq.empty():
    print(lq.get(),end=' ')

print()

pq=queue.PriorityQueue()
pq.put((400,"ABC"))
pq.put((100,"DEF"))
pq.put((50,"IJK"))
pq.put((300,"LMN"))

while not pq.empty():
    print(pq.get(),end=' ')