class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        dic = {}
        for row in mat:
            for i in row:
                if i not in dic:
                    dic[i] = 0
                dic[i] += 1
        
        min_res = float('inf')
        length = len(mat)
        
        for k,v in dic.items():
            if v == length:
                min_res = min(min_res, k)
        return min_res if min_res != float('inf') else -1

'''
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.
If there is no common element, return -1.
    
Solution: traverse all elements, store the conter in a dictionary
          select the smallest element which has a count == len(mat)
Time: O(n*m)
Space: O(n*m)
'''

