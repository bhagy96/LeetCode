class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int sum_m = 0;
        for (int r : rolls) {
            sum_m += r;
        }
        int sum_n = (rolls.size() + n) * mean - sum_m;
        if (sum_n < n || sum_n > n * 6) return {};
        vector<int> res(n, sum_n / n);
        for (int i = 0; i < sum_n % n; ++i) {
            res[i]++;
        }
        return res;
    }
};