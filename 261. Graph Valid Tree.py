class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # early detection edges_cnt with number of nodes
        if n - 1 != len(edges):
            return False
        
        # save all edges into hashtable
        edges_dict = {}
        for i, j in edges:
            print(i,j)
            if i not in edges_dict:
                edges_dict[i] = set()
            if j not in edges_dict:
                edges_dict[j] = set()
                
            edges_dict[i].add(j)
            edges_dict[j].add(i)
            
        # initialize dfs, using dfs to travese all nodes
        dfs = [0]
        visted = set([0])
        while dfs:
            tmp_dfs = []
            for node in dfs:
                for nei in edges_dict.get(node, []):
                    if nei not in visted:
                        visted.add(nei)
                        tmp_dfs.append(nei)
            dfs = tmp_dfs
            
        # check if all nodes are traversed
        return len(visted) == n
