class Solution(object):
    def judgeCircle(self, moves):
        if len(moves)%2 == 0:
            # hash table solution
            
#             dic = collections.Counter(moves)
#             return dic['U'] == dic['D'] and dic['L'] == dic['R']
        
            # count solution, faster
            return moves.count('U')==moves.count('D') and moves.count('R')==moves.count('L')
        return False
        
        
        
        # Initially, there is a Robot at position (0, 0). 
        # Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
