import collections
from random import randrange

que = []
q = collections.deque()

n = 20

que = [randrange(1, 20) for i in range(n)]
print(' '.join([str(s) for s in que]))

#element = q.popleft()
q.append(25)

print(' '.join([str(s) for s in que]))
#print(element)
