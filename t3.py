def top_sort(n,g,s):
    vistos=set()
    order=[]
    def t_sort(s):
        pilha=[]#criar uma pilha registrando o ultimo que eu visitei
        comeco=[s]
        ordem=[]
        while comeco:
            v=comeco.pop()#vertice vizinho
            if v not in vistos:
                comeco.extend(g[v])
                vistos.add(v)
                while pilha and v not in g[pilha[-1]]:
                    #sem ligacao entre o que esta na pilha com v(com a proxima
                    #iteracao do dfs)
                    ordem = [pilha.pop()] + ordem
                pilha.append(v)
        return pilha + ordem #add restantes da pilha
    
    for i in range(n):
        if i not in vistos:
            order = t_sort(i) + order
    return order

def contaCaminhos(g,n,s,t,f):
    v=[0 for i in range(n)]
    r=[0 for i in range(n)]
    y=[0 for i in range(n)]
    v[t]=1
    for i in range(n-2,-1,-1):
        for j in g[f[i]]: #cada adj
            if j[1]==0: #verde
                v[f[i]]+= v[j[0]]+r[j[0]]+y[j[0]]
            elif j[1]==1: #amarelo
                y[f[i]]+= v[j[0]]+y[j[0]]
            else: #vermelho
                r[f[i]]+= v[j[0]]
    return v[s]+r[s]+y[s]

n,m,s,t=[int(i) for i in input().split()]
g=[[] for i in range(n)]
#sem valores de cor para realizar o topological sort
f=[[] for i in range(n)]
for _ in range(m):
    a,b,c=[int(i) for i in input().split()] #a=local b=vizinho ao local c=cor
    g[a].append([b,c])
    f[a].append(b)       
#realizar ordem topologica,
f=top_sort(n,f,0)
#recorrencia
print(contaCaminhos(g,n,s,t,f))
