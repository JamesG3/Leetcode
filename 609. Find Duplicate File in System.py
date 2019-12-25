class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dic = {}
        
        for path in paths:
            data = path.split(' ')
            basepath, filenames = data[0], data[1:]
            for fn in filenames: 
                f, cont = fn.split('(')
                
                if cont not in content_dic:
                    content_dic[cont] = []
                content_dic[cont].append('{}/{}'.format(basepath, f))
            
        return [v for v in content_dic.values() if len(v) > 1]
            
            
            
'''
Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

Solution: hashtable
Time, Space: O(n)
'''
