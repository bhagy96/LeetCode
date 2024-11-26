class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        sh, th = defaultdict(int),defaultdict(int)
        #countS, countT = {}, {}
        for i in range(len(s)):
            sh[s[i]] +=1; #countS[s[i]] = 1 + countS.get(s[i], 0)
            th[t[i]] +=1;
        return sh==th;

        #python throws key error if normal dicts are use to mimic 
        #cpp behavior use defaultdict