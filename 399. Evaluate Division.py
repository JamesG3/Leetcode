class Node:
    def __init__(self, c):
        self.next = {}
        self.prev = {}
        self.c = c
    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_dic = {}
        
        # build graph
        for i, nodes in enumerate(equations):
            val = values[i]
            n1, n2 = nodes
            node1, node2 = node_dic.get(n1, Node(n1)), node_dic.get(n2, Node(n2))
            node_dic[n1] = node1
            node_dic[n2] = node2
            
            node1.next[n2] = val
            node2.prev[n1] = 1.0 / val
                    
        ans = []
        for n1, n2 in queries:
            if n1 not in node_dic or n2 not in node_dic:
                ans.append(-1)
                continue
                
            visted = set()
            dfs = {n1: 1}
            res = {}
            while dfs:                
                if n2 in dfs:
                    ans.append(dfs[n2])
                    break
                    
                tmp_dfs = {}
                for n, v in dfs.items():
                    if n in visted:
                        continue
                        
                    visted.add(n)
                    # traverse all next nodes
                    for nxt_n, nxt_val in node_dic.get(n, Node('')).next.items():
                        if nxt_n in visted:
                            continue
                        
                        tmp_dfs[nxt_n] = v * nxt_val
                    
                    # traverse all prev nodes
                    for prv_n, prv_val in node_dic.get(n, Node('')).prev.items():
                        if prv_n in visted:
                            continue
                        
                        tmp_dfs[prv_n] = v * prv_val
                dfs = tmp_dfs    
            
            # if no result found    
            if not dfs:
                ans.append(-1)
                    
        return ans
               
        
'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

Solution: BFS, Graph, Data Structure Design
'''
