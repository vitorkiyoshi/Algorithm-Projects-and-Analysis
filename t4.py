def find_set(pai,i):
    a=i
    while True:
        if pai[a]==a:
            return a
        else:
            a=pai[a]

def uniao(pai,prior,x,y):
    if prior[x]<prior[y]:
        pai[x]=y
    elif prior[y]>prior[x]:
        pai[y]=x
    else:
        pai[y]=x
        prior[u]+=1
#nn preciso necessariamente fazer grafo, basta saber se
#adiciono a aresta ou nao
n,m,k = [int(i) for i in input().split()]
E=[]
for _ in range(m):
    E.append([int(i) for i in input().split()])
E=sorted(E, key=lambda x: x[2])

pais=[i for i in range(n)]
pri=[0 for i in range(n)] #ranking
custo=0
comps=n
for i in E:
    if comps==k:
        print(custo)
        break
    u,v,w=i
    raizX = find_set(pais,u)
    raizY = find_set(pais,v)
    if raizX!=raizY:
        comps-=1
        uniao(pais,pri,raizX,raizY)
        custo+=w
