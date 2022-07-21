class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        for u,v in prerequisites:
            if u not in dic.keys():
                dic[u] = []
            if v not in dic.keys():
                dic[v] = []
            dic[u].append(v)
        visited = set()
        def dfs(cou):
            if cou in visited: return False
            if dic[cou]==[]: return True
            visited.add(cou)
            for pre in dic[cou]:
                if not dfs(pre): return False
            visited.remove(cou)
            dic[cou] = []
            return True
            
        for cou in dic.keys():
            if not dfs(cou): return False
        return True
            
            

        
        