class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount={}
        tcount={}
        if len(s)!=len(t):
            return False
        for character in s:
            scount[character]=scount.get(character,0)+1
        for character in t:
            tcount[character]=tcount.get(character,0)+1
        if scount==tcount:
            return True
        else:
            return False 