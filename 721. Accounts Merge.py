class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        e_u_dic = {}        # k:v == email: user_key   
        u_e_dic = {}        # k:v == user_key: set(emails)
        
        for i, act in enumerate(accounts):
            user = act[0]
            emails = act[1:]
            
            users = set()
            exist_emails = set()
            
            # check if there is any email existed in other accounts
            for e in emails:
                if e in e_u_dic:
                    users.add(e_u_dic[e])
                    exist_emails.add(e)
            
            # use this to prevent same name but different person
            user_key = (user, i)
            
            # all given emails in the current account don't exist in current data, create new entry for this account
            if not users:
                u_e_dic[user_key] = set(emails)
                for e in emails:
                    e_u_dic[e] = user_key
            
            # union all existing record into one entry
            else:
                # collect all emails from those accounts need to be merged
                email_set = set()
                for u in users:
                    email_set.update(u_e_dic[u])
                    del u_e_dic[u]
                email_set.update(set(emails))
                u_e_dic[user_key] = email_set
                
                for e in email_set:
                    e_u_dic[e] = user_key
        
        res = []
        for k, v in u_e_dic.items():
            res.append([k[0]] + sorted(list(v)))
        return res            

'''
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.


Solution: Union Find, hash table, two hash table, merging during searching
Time: O(nlogn)
Space: O(n)
'''
