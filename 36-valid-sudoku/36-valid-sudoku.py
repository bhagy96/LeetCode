class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
        
#         def loop(si,sj, ei, ej, flag = 0):
#             # print("****",si,sj, ei, ej)
#             for i in range(si,ei):
#                 dic = {}
#                 ogi = i
#                 for j in range(sj,ej):
#                     # print("i,j ", i,j)
#                     if flag: i,j = j,ogi
#                     # print("i,j ", i,j)
#                     # print(si,sj,i,j,board[i][j], dic)
#                     if board[i][j]!=".":
#                         if board[i][j] in dic.keys():
#                             return False
#                         else:
#                             dic[board[i][j]] = ""
#                 if flag: i = ogi
#             return True
#         op = loop(0,0, len(board), len(board[0]),0)
#         if op==False: return False
#         # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#         op = loop(0,0, len(board[0]), len(board),1)
#         if op==False: return False
#         # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#         i,j = 0,0               
#         while i<9:
#             while j<9:
#                 op = loop(i,j, i+3, j+3,0)
#                 if op==False: return False
#                 j +=3
#             i += 3
            
#         return True
                
                