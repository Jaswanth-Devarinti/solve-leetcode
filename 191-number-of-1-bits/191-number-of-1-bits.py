class Solution:
    def hammingWeight(self, n: int) -> int:
        bi = str(bin(n))[2:]
        #print(bi)
        return str(bi).count('1')