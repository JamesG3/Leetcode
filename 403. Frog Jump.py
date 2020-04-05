class Solution:
    def canCross(self, stones: List[int]) -> bool: 
        paths = {stone: set() for stone in stones}
        paths[0].add(0)
        
        for i, stone in enumerate(stones):
            path2here = list(paths[stone])
            for p in path2here:
                for nxtstone in stones[i+1:]:
                    if p-1 <= (nxtstone-stone) <= p+1:
                        paths[nxtstone].add(nxtstone-stone)
                    
                    # early termination
                    elif (nxtstone-stone) > p+1:
                        break      
        return len(paths[stones[-1]]) != 0
                            
'''
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.

Solution: 
    DP, for each stone, look forward all the rest of stones (with early termination)
    If can reach that stone, add the distance to that stone's value set
    For each of the paths which can reach the current stone, look forward again to see if there is any stone can reach
    
Time: O(n^2)
Space: O(n^2)
'''
