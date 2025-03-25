#include <vector>
#include <algorithm>

void sort_ascending(vector<int> &nums1)
{
    sort(nums1.begin(), nums1.end());
}

int removeElement(vector<int>& nums, int val) {
    nums.erase(std::remove(nums.begin(), nums.end(), val), nums.end());
    return nums.size();
}

int removeDuplicates(vector<int>& nums) {
    nums.erase(std::unique(nums.begin(), nums.end()), nums.end());
    return nums.size();
}
