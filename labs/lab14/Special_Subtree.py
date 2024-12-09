N, E = map(int, input().split())

edges = [[] for i in range(N + 1)]

for e in range(E):
    x, y, r = map(int, input().split())
    edges[x].append((y, r))
    edges[y].append((x, r))                      

S = {x + 1 for x in range(N)}
T = set()
E = 0;

T.add(S.pop())
    
#print(sorted(edges, key = lambda x: x[2]))
while S:
       
    minStart = -1;
    minEnd = -1;
    minCost = float("inf");
    
    for v in T:
        for e in edges[v]:            
            if e[0] in S:
                if e[1] < minCost:
                    minStart = v
                    minEnd = e[0]
                    minCost = e[1]
                    
    if minCost < float("inf"):
        E += minCost
        S.remove(minEnd)
        T.add(minEnd)
        
print(E)