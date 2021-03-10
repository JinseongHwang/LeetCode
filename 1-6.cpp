#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> mp;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int &A = nums[i];
            int B = target - A;

            if (mp.find(B) != mp.end()) {
                result.push_back(i);
                result.push_back(mp[B]);
                break;
            }

            mp[A] = i;
        }

        return result;
    }
};