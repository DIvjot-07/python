from collections import Counter,defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """ result=[]
        n=len(strs)
        visit=[False]*n
        for low in range(n):
            if(visit[low]):
                continue
            out=[strs[low]]
            visit[low]=True
            for i in range(low+1,n):
                if(not visit[i] and Counter(strs[low]) == Counter(strs[i])):
                    out.append(strs[i])
                    visit[i]=True
            result.append(out)

        return result """
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  