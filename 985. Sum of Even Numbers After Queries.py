class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        cur_sum = 0
        for n in A:
            if n%2 == 0:
                cur_sum += n
                
        res = []
        for m, i in queries:
            num = A[i]
            if num%2 == 0:
                cur_sum -= num
            
            if (m+num)%2 == 0:
                cur_sum += m+num
            
            A[i] = m+num
            res.append(cur_sum)
        return res
            
            
'''
We have an array A of integers, and an array queries of queries.
For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.
(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

Solution: Traverse and mark
Time, Space: O(n)
'''
