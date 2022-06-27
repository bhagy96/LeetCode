class Solution:
    def simplifyPath(self, path: str) -> str:
        i=1
        ret = ''
        direc = []
        path += '/'
        while i<len(path):
            temps = ''
            # print(i,path[i])
            while path[i]!='/':
                
                temps += path[i]
                i+=1
            # print(temps)
            if direc and temps=='..':
                direc.pop()
            elif temps and temps!='.' and temps!='..':
                direc.append('/'+temps)                          
            i+=1
        if not direc:
            return '/'
        return "".join(direc)
        
        # if not ret:
        #     return '/'
        # if ret[-1]=='/':
        #     return '/'+ret[:-1]
        # return '/'+ret