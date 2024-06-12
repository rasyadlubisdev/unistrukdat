def dfs(curr_vrtx, max_vrtx, adj_list, visited):
    visited[curr_vrtx] = True
    global max_final
    for i in adj_list[curr_vrtx]:
        if not visited[i]:
            dfs(i, max_vrtx + 1, adj_list, visited)
    max_final = max(max_vrtx, max_final)
    visited[curr_vrtx] = False

V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]
visited = [False] * V
max_final = 0

for _ in range(E):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

start = int(input())

dfs(start, max_final, adj_list, visited)

print(max_final)