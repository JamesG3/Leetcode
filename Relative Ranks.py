#A bit different with the original exercise: this one can calculate the rank even if the input has duplicate scores.
class Solution(object):
    def findRelativeRanks(self, nums):
        dic = {}
        
        for n in nums:              #count the number of same score in nums
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        #print dic
        add = 1
        thisplus = nextplus = 0
        for m in sorted(list(set(nums)))[::-1]:         #for scores from high to low, find them in the dic, calculate the rank and save in the dic
            if dic[m] != 1:
                nextplus+=dic[m]-1
            dic[m] = add+thisplus
            add+=1
            thisplus = nextplus
        #print dic
        
        ans = []                #find the rank in dic, output the rank
        for item in nums:
            if dic[item] == 1:
                ans.append("Gold Medal")
            elif dic[item] == 2:
                ans.append("Silver Medal")
            elif dic[item] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(dic[item]))
                
        return ans
        
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        # Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
        # N is a positive integer and won't exceed 10,000.
        # All the scores of athletes are guaranteed to be unique.
