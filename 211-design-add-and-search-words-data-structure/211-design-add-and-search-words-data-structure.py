# class TrieNode:
    
#     def __init__(self):
#         self.childern = {}
#         self.endword = False
    
# class WordDictionary:

#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
        
#         cur = self.root
#         for c in word:
#             if c not in cur.childern:
#                 cur.childern[c] = TrieNode()
#             cur = cur.childern[c]
#         cur.endword = True

#     def search(self, word: str) -> bool:
        
#         def dfs(cur, j):
            
#             for i in range(j, len(word)):
#                 c = word[i]
#                 if c=='.':
#                     for child in cur.childern.values():
#                         if dfs(child, i+1):
#                             return True
#                         return False                        
#                 else:
#                     if c not in cur.childern:
#                         return False
#                     cur = cur.childern[c]
#             return cur.endword
#         return dfs(self.root,0)


# class TrieNode:
    
#     def __init__(self):
#         self.childern = {}
#         self.endword = False
    
# class WordDictionary:

#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         cur = self.root
#         for c in word:
#             if c not in cur.childern:
#                 cur.childern[c] = TrieNode()
#             cur = cur.childern[c]
#         cur.endword = True

#     def search(self, word: str) -> bool:
        
#         def dfs(cur, j):
            
#             for i in range(j, len(word)):
#                 c = word[i]
#                 if c == '.':
#                     for child in cur.childern.values():
#                         if dfs(child, i+1):
#                             return True
#                         return False
#                 else:
#                     if c not in cur.childern:
#                         return False
#                     cur = cur.childern[c]
#             return cur.endword
            
#         return dfs(self.root,0)


# class TrieNode:
#     def __init__(self):
#         self.children = {} # a : TrieNode
#         self.word = False

# class WordDictionary:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def addWord(self, word: str) -> None:
#         cur = self.root
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
#         cur.word = True
        
    
        
#     def search(self, word: str) -> bool:
#         def dfs(j, root):
#             cur = root

#             for i in range(j, len(word)):
#                 c = word[i]
#                 if c == ".":
#                     for child in cur.children.values():
#                         if dfs(i + 1, child):
#                             return True
#                     return False
#                 else:
#                     if c not in cur.children:
#                         return False
#                     cur = cur.children[c]
#             return cur.word
        
#         return dfs(0, self.root)

    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1
        
    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.end_node
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)






















# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)