import sys
N =7
s=0
g=[None for x in range(N+1)]
g[0]=[(1,9),(2,10)]
g[1]=[(0,9),(3,10),(4,5),(6,3)]
g[2]=[(0,10),(3,9),(4,7),(5,2)]
g[3]=[(1,10),(2,9),(5,4),(6,8)]
g[4]=[(1,5),(2,7),(6,1)]
g[5]=[(2,2),(3,4),(6,6)]
g[6]=[(1,3),(3,8),(4,1),(5,6)]
# g[0] = [(1,8),(2,3)]
# g[1] = [(0,8),(2,4),(3,2)]
# g[2] = [(0,3),(1,4),(3,9)]
# g[3] = [(1,2),(2,9)]
visited = [False for x in range(N+1)]
D = [sys.maxsize for x in range(N+1)]
D[s] = 0
previous = [None for x in range(N+1)]
previous[s] = s

for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True
    for w, wt in g[m]:
        if not visited[w]:
            if wt <D[w]:
                D[w] = wt
                previous[w] = m
print("최소신장트리:",end="")
mst_cost = 0
for i in range(1,N):
    print('(%d,%d)'% (i,previous[i]),end="")
    mst_cost += D[i]
print("\n최소신장트리 가중치",mst_cost)