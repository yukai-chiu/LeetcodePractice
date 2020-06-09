#hash map
#Time: O(n)
#Space: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        #first try
        #counter 
        if not s:
            return 0
   
        longest = 0
        counter = Counter()
        start = 0
        for i, c in enumerate(s):
            counter[c]+=1
            while len(counter) > k:
                counter[s[start]]-=1
                if counter[s[start]] ==0:
                    del counter[s[start]]
                start+=1
            longest = max(longest, i-start+1)
        return longest