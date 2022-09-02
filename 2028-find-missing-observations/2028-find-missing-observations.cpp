class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        
        int m = rolls.size();
        int tot = mean * (n + m);
        
        int left = tot;
        for(auto& r: rolls) {
            left -= r;
        }
        
        if(left < n || n*6 < left) return {};
        
        int rest = (left - n);
        
        vector<int> res;
        for(int i = 0; i < n; i++ ) {
            int mn = min(5, rest);
            res.push_back( mn + 1 );   
            rest -= mn;
        }
        
        return res;
    }
};