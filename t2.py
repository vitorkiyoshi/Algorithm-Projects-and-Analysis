def verif(a): #a = adj, v=n
    gb=0
    gr=0
    for i in a:
        for j in i: #percorrendo arestas do vertice
            if i[j][0]==1:
                gb+=1
            else:
                gr+=1
        if gb!=gr:
            return False
        else:
            gb=0
            gr=0
    return True
            

def construirMaximal(adj,v,cor_i):
    #n vertices passados, v=vertice inicio, cor_i=cor inicial aresta, 
    #'primeira iteracao'
    g=[v]
    t=1
    vertice=v
    c=cor_i
    for i in adj[v]: #i arestas de v
        if adj[v][i][0]==c and adj[v][i][1]==0:#nao visitada e na cor desejada
            g.append(i)
            del(adj[vertice][i])
            del(adj[i][vertice])
            vertice=i
            c=not c
            t+=1
            break
    #demais ate achar v novamente
    while not(vertice==v and c==cor_i): #cor que desejo igual a cor inicial
        for i in adj[vertice]: #i arestas de v
            if adj[vertice][i][0]==c and adj[vertice][i][1]==0:#nao visitada e na cor desejada
                g.append(i)
                del(adj[vertice][i])
                del(adj[i][vertice])
                vertice=i
                c=not c
                t+=1
                break
    return adj,g,t

def verifR(g,adj,n_g):
    # dos vertices de g, achar algum com aresta vaga e cor dif da passada
    c=0 #cor anterior inicia em 0
    for i in range(1,n_g):
        v = g[i]#vertice
        pas=g[i-1]#vertice vizinho passado
        #cor do anterior
        for j in adj[v]:
            if adj[v][j][0]!=c: 
                return v, not c,i
        c=not c
    return False

def montar(adj,v,m): # a=adj, v=n, arest=m
    v=0
    c=0
    s=0
    adj, g , x = construirMaximal(adj,v,c)
    grafo=g
    s+=x
    while True:
        if s>=m:
            return grafo
        b = verifR(grafo,adj,s)
        if not b:
            return grafo
        else:
            v,c,p=b
            adj, g , x = construirMaximal(adj,v,c)
            grafo = grafo[:p] + g[:-1]+ grafo[p:]
            s += x-1 #por deletar um elemento
    #return n,adj atualizada, vertice para criar prox subgrafo,
    #cor da aresta a ser iniciada,grafo


n,m=[int(i) for i in input().split()] #n vertices m arestas
adj=[{} for i in range(n)] #para cada vertice seus vizinhos, com cor e se passou
for i in range(m):
    a1,a2,c=[int(i) for i in input().split()]
    adj[a1][a2]=[c,0] #vizinho, cor, passado
    adj[a2][a1]=[c,0]
if not verif(adj):
    print("Não possui trilha Euleriana alternante")
else:
    print(*montar(adj,n,m))
##FORMAS DE OTIMIZACAO: RETIRAR ORDEM DE N2 BASTANDO ADICIONAR AO VERTICE DE ADJ UM PARAMETRO GRAU