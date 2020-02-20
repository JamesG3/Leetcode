class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        if not K:
            return sum(sweetness)
        
        big = sum(sweetness) / K
        small = 1
        
        while small <= big:
            mid = (small + big) // 2
            cur_cnt = 0
            cur_swt = 0
            for s in sweetness:
                cur_swt += s
                if cur_swt >= mid:
                    cur_swt = 0
                    cur_cnt += 1
                # early termination
                if cur_cnt > K:
                    break
            # mid too small
            if cur_cnt > K:
                small = mid + 1
            # mid is big
            else:
                big = mid - 1
        return int(big)
                
'''
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.
You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.
Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Solution: Binary Search on the result in range(1, avg(sum(swetness)) + 1)
Time: O(nlogm)
Space: O(1)
'''           
    
