class Solution:
    def minCount(self, coins) :
        n=0
        for i in coins:
            if i%2==0:
                n+=i//2
            else:
                n+=i//2+1
        return  n

l=[2,3,10]
print(Solution().minCount(l))
