class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length())
        {
            return false;
        }

        unordered_map<char, int> sh;
        unordered_map<char, int> th;
        for(int i=0; i<s.length();i++)
        {
            sh[s[i]] += 1;
            th[t[i]] += 1;
        }
        return sh==th;
    }
};