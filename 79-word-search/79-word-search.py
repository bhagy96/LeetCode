
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

        
class Solution:
    def exist(self, board: List[List[str]], acword: str) -> bool:
        root = TrieNode()
        # for w in words:
        root.addWord(acword)
        self.found = False
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                board[r][c] not in node.children  or
                (r, c) in visit):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                self.found = True
                return
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
                if self.found:
                    return True
        return False