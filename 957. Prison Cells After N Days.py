class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        pattern = {}
        
        while N > 0:
            tp = tuple(cells)
            if tp in pattern:
                N %= pattern[tp] - N
            else:
                pattern[tp] = N
                
            # this means after we find the cycle, the current cell status is exactly the last status after N days, break
            if N == 0:
                break
            
            # traverse all the rest of the status, after we reduce N to the last cycle
            tmp_cells = []
            for i in range(1, len(cells) - 1):
                if cells[i+1] == cells[i-1]:
                    tmp_cells.append(1)
                else:
                    tmp_cells.append(0)
            cells = [0] + tmp_cells + [0]
            N -= 1
            
        return cells

'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Solution: Hasttable, cycle, math
Time: O(2^K), K is the nubmer of cells in prision
'''
