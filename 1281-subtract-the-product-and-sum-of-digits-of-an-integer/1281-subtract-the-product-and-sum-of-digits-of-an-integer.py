class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul,add=1,0
        while(n>0):
            rem = n%10
            n=n//10
            mul = mul*rem
            add = add+rem
        return mul-add
        