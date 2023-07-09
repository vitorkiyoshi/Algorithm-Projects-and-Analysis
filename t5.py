n=int(input())
v=[int(i) for i in input().split()]
m=int(input())
w=[]
for i in range(m):
    w.append([int(i) for i in input().split()])
#initializeSingleSource
pi=[None for i in range(n)]
d=[float('-inf') for i in range(n)]
d[0]=0
def relax(a,b):
    x = d[a]+v[b]
    if d[b]< x and x>-100:#se for uma aresta possivel
        d[b] = x
        pi[b] = a
def BellmanFord():
    cp=False
    for i in range(n-1):
        for j in w:
            relax(j[0],j[1])
    for i in w:
        if d[i[1]]<d[i[0]]+v[i[1]]:
            cp=True
            break
    if (cp and d[n-1]!=float('-inf')) or d[n-1]>-100:
        return "possible"
    return "impossible"
print(BellmanFord())
    
