class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int m = (left + right) / 2;

            if (nums[m] == target) {return m;}
            if (nums[m] < target) {left = m + 1;}
            else {right = m;}
        }
        
        return left;
    }
}
