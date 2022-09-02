class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        long long sum=accumulate(begin(rolls),end(rolls),0);
        long long temp=(n+rolls.size())*1ll*mean;
        temp-=sum;
        int a=(temp+(n-1))/n;
        if(a>6||temp<n)return {};
        sum=temp/n;
        vector<int> ans(n,sum);
        temp%=n;
        while(temp)
        {
            ans[temp]++;
            temp--;
        }
        return ans;
    }
};