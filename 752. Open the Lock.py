class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visted = set()
        deadends = set(deadends)
        
        dfs = ['0000']
        count = -1
        while dfs:
            count += 1
            tmp_dfs = []
            for item in dfs:
                if item in visted or item in deadends:
                    continue
                visted.add(item)
                
                if item == target:
                    return count
                
                neighs = self.get_neigh(item)
                for neigh in neighs:
                    if neigh in visted or neigh in deadends:
                        continue
                    tmp_dfs.append(neigh)
            dfs = tmp_dfs        
        return -1
                                
                
    def get_neigh(self, string):
        res = []
        for i in range(4):
            num = int(string[i])
            nums = [num+1, num-1]
            for num in nums:
                if num == 10:
                    updated_num = 0
                elif num == -1:
                    updated_num = 9
                else:
                    updated_num = num
                
                res.append(string[:i] + str(updated_num) + string[i+1:])
        return res
                    
            
'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Solution: BFS
Time, Space: O(n)
'''        
