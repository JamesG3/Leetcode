
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        Solution: Hashtable and sort
        Time: O(nlogm)
        Space:O(n*m)
        """
        dic = {}
        for student, score in items:
            if student not in dic:
                dic[student] = [score]
            else:
                dic[student].append(score)
                
        res = []
        for i, scores in dic.items():
            score = sum(sorted(scores)[-5:])
            length = len(scores)
            max_len = 5 if length > 5 else length
            avg_score = score / 5 if length > 5 else score / length
            res.append([i, avg_score])
            
        return res
        
        
# Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
