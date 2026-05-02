class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=set(list(s))
        b=set(list(t))
        if a!=b:
            return False
        c=Counter(s)
        d=Counter(t)
        for i in c:
            if c[i]!=d[i]:
                return False
        return True