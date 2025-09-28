from collections import deque

N = 100
vis = [False] * N
parrent = [-1] * N
graph = [[] for _ in range(N)]

def main():
    nodes , edges = map(int,input().split())

    for _ in range(edges):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    source = int(input("Enter source node:"))
    target = int(input("Enter target node:"))
    bfs(source)

    if not vis[target]:
        print("No path")
        return
    
    path = []

    curr = target
    while curr !=-1:
        path.append(curr)
        curr = parrent[curr]

    path.reverse()

    print('->'.join(map(str,path)))
    
def bfs(source):
    q = deque()
    q.append(source)
    vis[source] = True

    while q:
        curr = q.popleft()
        for child in graph[curr]:
            if not vis[child]:
                q.append(child)
                vis[child] = True
                parrent[child] = curr



if __name__ == "__main__":
    main()