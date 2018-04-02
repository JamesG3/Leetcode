class Codec:

    def encode(self, strs):

        return ''.join([s.replace(':', '::') + '-:-' for s in strs])
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        

    def decode(self, s):
        return [n.replace('::', ':') for n in s.split('-:-')[:-1]]


        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


