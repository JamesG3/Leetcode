class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        types = set([])
        for can in candies:
            types.add(can)
        return min(len(candies) // 2, len(types))
        
        
'''
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Solution: Hashset
    - sis will get all kinds of candies if there are enough
    - if there is only one candy for each category, sis can get half of all kinds of candies
    
Time, Space: O(n)
'''
