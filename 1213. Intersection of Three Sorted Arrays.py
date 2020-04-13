class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        cnter = {}
        for arr in [arr1, arr2, arr3]:
            for n in arr:
                cnter[n] = cnter.get(n, 0) + 1
        for k, v in sorted([[k, v] for k,v in cnter.items()]):
            if v == 3:
                res.append(k)
        return res

'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Solution: Hash table
Time: O(n)
Space: O(n)
'''
