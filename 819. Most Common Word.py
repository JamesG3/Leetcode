from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = ''.join([' ' if not ('a' <= _ <= 'z') else _ for _ in paragraph]).split(' ')
        paragraph = filter(lambda x: x != '', paragraph)
        paragraph = [word.strip() for word in paragraph]
        banned = [word.lower() for word in banned]
        word_cnt = Counter(paragraph)
        for w in banned:
            if w in word_cnt:
                del word_cnt[w]
        max_cnt = max(word_cnt.values())
        for k, v in word_cnt.items():
            if v == max_cnt:
                return k
        
'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Solution: Hashtable, String clean
Time, Space: O(n)
'''    
