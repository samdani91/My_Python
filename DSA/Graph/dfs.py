N = 100
vis = [False] * N
parrent = [-1] * N
graph = [[] for _ in range(N)]


def main():
    nodes,edges = map(int,input().split())

    for _ in range(edges):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    source = int(input("Enter source node:"))
    target = int(input("Enter target node:"))

    dfs(source)

    if not vis[target]:
        print("No path")
        return
    
    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        curr = parrent[curr]

    path.reverse()
    print('->'.join(map(str,path)))



def dfs(source):
    vis[source] = True

    for child in graph[source]:
        if not vis[child]:
            parrent[child] = source
            dfs(child)




if  __name__ == "__main__":
    main()