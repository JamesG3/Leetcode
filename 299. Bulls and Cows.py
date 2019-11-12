from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        secret_dic = Counter(secret)
        for i, n in enumerate(guess):
            if n == secret[i]:
                if secret_dic[n] == 0:
                    secret_dic[n] += 1
                    B -= 1
                secret_dic[n] -= 1
                A += 1
                continue
                
            if secret_dic.get(n, 0) > 0:
                B += 1
                secret_dic[n] -= 1
                
        return '{}A{}B'.format(A, B)
                
'''
bulls - how many digits in said guess match your secret number exactly in both digit and position 
cows - how many digits match the secret number but locate in the wrong position
'''
