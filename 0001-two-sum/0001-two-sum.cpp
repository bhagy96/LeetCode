class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> umap;
        vector<int> res;
        for(int i=0; i<nums.size(); i++)
        {
            int diff = target-nums[i];
            if(umap.find(diff)!=umap.end())
            {
                res.push_back(umap[diff]);
                res.push_back(i);
                return res;
            }
            umap[nums[i]] = i;
                
        }
        return res;
    }
};