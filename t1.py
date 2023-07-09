n=int(input())
degrees=[int(i) for i in input().split()]
nodes = list(range(len(degrees)))
adj = [[] for node in nodes]
while sum(degrees) != 0:
    head = degrees[nodes[0]]
    head_pos = nodes[0]
    i = 1
    seq = True
    for node in nodes[1:]:
        if head == 0: #Não é seq graf
            break
        elif degrees[node] == 0:
            seq = False
            break
        else:
            adj[head_pos].append(node)
            adj[node].append(head_pos)
            degrees[node] -= 1
            head -= 1
    if head != 0 or (not seq):
        seq = False
        break
    else:
        degrees[head_pos] = 0
    nodes = sorted(nodes[1:], key=degrees.__getitem__, reverse=True)
if seq:
    for a in adj:
        a = sorted([i+1 for i in a])
        print(*a, sep=" ")
else:
    print("Não é sequência gráfica!")
        
    
