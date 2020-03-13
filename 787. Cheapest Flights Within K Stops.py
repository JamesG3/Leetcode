class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.dst_map = {}
        for i, j, p in flights:
            if i not in self.dst_map:
                self.dst_map[i] = [[j, p]]
            else:
                self.dst_map[i].append([j, p])
        
        self.dst = dst
        self.price = float('inf')
        self.dfs(src, K, 0, set())
        return self.price if self.price != float('inf') else -1
                
        
    def dfs(self, node, k, p, visted):
        if k == -2:
            return

        if node == self.dst:
            self.price = min(self.price, p)
            return
        
        if self.price <= p:
            return

        for nn, pp in self.dst_map.get(node, []):
            if nn in visted:
                continue

            visted.add(nn)
            self.dfs(nn, k-1, pp+p, visted)
            visted.remove(nn)
'''
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Solution: Graph DFS, Dijkstra's
'''
