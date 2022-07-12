   
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endword = True
        
    def search(self, word):
        
        def dfs(cur, i):
            if i==len(word):
                return cur.endword
            if word[i]==".":
                for child in cur.children:
                    if dfs(cur.children[child], i+1): return True
            if word[i] in cur.children:
                return dfs(cur.children[word[i]], i+1)
            return False
        return dfs(self.root, 0)
    
    
# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)