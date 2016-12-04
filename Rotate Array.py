class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        if k!=0:
            tem=nums[-k:]               #rotate part of nums
            nums[-len(nums)+k:] = nums[:len(nums)-k]        #in-place replace elements in nums
            nums[:k] = tem              #in-place replace the rotate part
        
        
      #Rotate an array of n elements to the right by k steps.
      #For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        

"""

    #java reverse solution
    #use O(n) time and O(1) extera space(no extera space)
    #rotate 3 times
    #1 2 3 4 5 6 7
    #7 6 5 4 3 2 1
    #5 6 7 4 3 2 1
    #5 6 7 1 2 3 4
    
    public class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
    }



    #TLE solution (usign O(1) extra space)
    def rotate(self, nums, k):
        
        k=k%len(nums)
        while k != 0:
            k-=1
            tem=nums[-1]
            for counter in xrange(len(nums)-1,-1,-1):
                nums[counter]=nums[counter-1]
            nums[0]=tem
            
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
"""
        
        
