class Solution:
    def simplifyPath(self, path: str) -> str:
        # perfect
#         stack = []
#         for elem in path.split("/"):
#             if stack and elem == "..":
#                 stack.pop()
#             elif elem not in [".", "", ".."]:
#                 stack.append(elem)
                
#         return "/" + "/".join(stack)
    
    # my solution
        i=1
        ret = ''
        direc = []
        path += '/'
        while i<len(path):
            temps = ''
            while path[i]!='/':                
                temps += path[i]
                i+=1
            if direc and temps=='..':
                direc.pop()
            elif temps and temps!='.' and temps!='..':
                direc.append('/'+temps)                          
            i+=1
        if not direc:
            return '/'
        return "".join(direc)