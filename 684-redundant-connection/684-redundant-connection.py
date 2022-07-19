class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            # print(source,target,graph[source])
            if source not in visited:
                # print('nv',source)
                visited.add(source)
                if source == target: return True
                for nei in graph[source]:
                    if dfs(nei, target):
                        return True

        for u, v in edges:
            visited = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
            # print(graph)