class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist_dic = {}
        for u, v, w in times:
            if u not in dist_dic:
                dist_dic[u] = {}
            dist_dic[u][v] = min(w, dist_dic[u].get(v, float('inf')))
        
        
        dist = {n: float('inf') for n in range(1, N+1)}
        visted = [False] * (N+1)
        dist[K] = 0
        
        while True:
            cand_node = -1
            cand_dist = float('inf')
            # find the most nearest node from the current traversed nodes, use this node to expand neighbors
            for i in range(1, N+1):
                if not visted[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            
            if cand_node < 0:
                break
                
            visted[cand_node] = True
            for nei, d in dist_dic.get(cand_node, {}).items():
                dist[nei] = min(dist[nei], dist[cand_node] + d)
                
        res = max(dist.values())
        return -1 if res == float('inf') else res

    
'''
There are N network nodes, labelled 1 to N.
Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Solution: Graph traverse, Dijkstra's algorithm
            In every round, find out the most nearest node from the current visted node clusters, use this node to expand all neighbors
            
Time: O(n^2)
Space: O(n^2)
'''
        
            
