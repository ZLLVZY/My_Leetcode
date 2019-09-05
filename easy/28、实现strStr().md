28、实现strStr():https://leetcode-cn.com/problems/implement-strstr/
方法一：
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        if n==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+n]==needle:
                return i
        return -1
遍历haystack，看第i位开始到i+n位是否等于needle，是在返回i，遍历结束都没返回则返回-1
方法二：
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
调用.index方法
方法三：
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
调用find方法