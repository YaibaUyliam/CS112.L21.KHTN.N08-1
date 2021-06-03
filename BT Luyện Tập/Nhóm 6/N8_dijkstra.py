import sys

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[max][0]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

def dijkstra(Graph, n):

    A, B, K = map(int, sys.stdin.readline().strip().split())

    Q = PriorityQueue()
    Q.insert((0, A))
    visited = set()
    cnt = 0
    while not Q.isEmpty():
        t, v = Q.delete()
       
        if t > K:
            break
        if v == B:
            if t == K:
                cnt += 1
            continue
        for u, w in Graph[v]:
            if (v, u) not in visited:
                Q.insert((w + t, u))
                visited.add((u, v))

    if cnt == 0:
        print(-1)
    else:
        print(cnt)

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    Graph = []
    for i in range(n):
        A = []
        Graph.append(A)
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        Graph[u].append((v, w))
        Graph[v].append((u, w))
    dijkstra(Graph, n)

main()
