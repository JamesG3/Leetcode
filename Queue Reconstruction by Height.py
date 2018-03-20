class Solution(object):
    # concise solution, O(n^2)
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
    
    
    
    def reconstructQueue(self, people):
        res = []
        length = len(people)
        if length == 0:
            return []
        
        people = sorted(people)[::-1]
        M = people[0][0]
        
        i = 0
        
        while i != length:                      #initialize the first part
            if people[i][0] == M:
                res = [people[i]] + res
                i+=1
            else:
                M = people[i][0]
                break
            
        tem = []
        while i != length:                      #for each group of people with the same height, append them into a tem list
            if people[i][0] == M:
                tem.append(people[i])
            else:
                while len(tem) != 0:
                    ap = tem.pop()              # insert people into array with asc order
                    index = ap[1]
                    res = res[0:index] + [ap] + res[index:]
                M = people[i][0]
                tem.append(people[i])
            i += 1
            
        while len(tem) != 0:                # insert the last part
            ap = tem.pop()
            index = ap[1]
            res = res[0:index] + [ap] + res[index:]
                
        return res
        
        
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
        #The number of people is less than 1,100.
