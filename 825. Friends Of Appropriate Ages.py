class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnter = {}
        for age in ages:
            cnter[age] = cnter.get(age, 0) + 1
        
        people = sorted([[age, cnt] for age, cnt in cnter.items()])[::-1]
        res = 0
        
        for i, meta in enumerate(people):
            age, cnt = meta
            if cnt != 1:
                if not any([age > age, age <= 0.5 * age + 7, age > 100 and age < 100]):
                    res += cnt * (cnt-1)
            
            for age2, cnt2 in people[i+1:]:
                if not any([age2 > age, age2 <= 0.5 * age + 7, age2 > 100 and age < 100]):
                    res += cnt * cnt2
        
        return res
        
'''
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.
How many total friend requests are made?

Solution: Hash table, sort
Time: O(1)
Space:O(1)
'''
        
