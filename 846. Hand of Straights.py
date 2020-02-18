from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = Counter(hand)
        min_stack = sorted(set(hand))
        
        while min_stack:
            cur_min = min_stack[0]
            cnt = counter.get(cur_min, None)
            if not cnt:
                min_stack.pop(0)
                continue
            
            # traverse the 3 consecutive cards
            for i in range(cur_min, cur_min + W):
                if counter[i]:
                    counter[i] -= 1
                else:
                    return False
        return True
                    
                
'''
Alice has a hand of cards, given as an array of integers.
Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
Return true if and only if she can.

Solution: Stack, Hashtable, Simulation
Time: O(n * w)
Space: O(n)
'''
