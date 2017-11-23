class Solution(object):
    def findShortestSubArray(self, nums):
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        Max = 0
        for times in dic.values():
            Max = max(Max, times)
        
        numList = []
        for number in dic:
            if dic[number] == Max:
                numList.append(number)
            
        dic.clear()
        index = 0
        for number in nums:
            if number in dic:
                dic[number][0] += 1
                if dic[number][0] == Max:
                    dic[number][-1] = index - dic[number][1] + 1
            else:
                dic[number] = [1, index, 1]
            index += 1
        
        miniDis = float('Inf')
        for num in numList:
            miniDis = min(miniDis, dic[num][2])
        return miniDis
        
        
#         reverseNums = nums[::-1]
        
#         miniDis = float('Inf')
#         Length = len(nums)
#         for num in numList:
#             distance = Length - reverseNums.index(num) - nums.index(num)
#             miniDis = min(miniDis, distance)
        
        # return miniDis
                
            
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
        #Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
