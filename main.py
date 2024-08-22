class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        return haystack.find(needle)


solution = Solution()
haystack = "sadbutsad"
needle = "sad"

result = solution.strStr(haystack, needle)

print(result)
