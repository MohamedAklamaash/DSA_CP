def count_provinces(isConnected):
    def dfs(node):
        visited[node] = True
        for neighbor in range(len(isConnected)):
            if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    n = len(isConnected)
    visited = [False] * n
    province_count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            province_count += 1

    return province_count

isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

print("Number of Provinces:", count_provinces(isConnected))

