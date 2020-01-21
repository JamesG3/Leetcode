class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        length = len(s)
        dfs = [0]
        visited = [0] * length
        
        while dfs:
            start = dfs.pop()
            if visited[start] == 1:
                continue
            
            # prevent duplicated travsersal
            visited[start] = 1
            for i in range(start+1, length+1):
                substr = s[start:i]
                if substr in word_dict:
                    dfs.append(i)
                    if i == length:
                        return True                    
        return False
                    

        
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Solution: DFS, Find if there is a way to reach the last letter using given dictionary
Time: O(n^2)
Space: O(n)
'''
