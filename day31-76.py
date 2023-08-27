class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        tc={}
        windowc={}
        for i in t:
            tc[i]=tc.get(i,0)+1
        have=0
        need=len(tc)
        res=[-1,-1]
        reslen=float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            windowc[c]=windowc.get(c,0)+1

            if c in tc and tc[c]==windowc[c]:
                have+=1
            
            while need==have:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                windowc[s[l]]-=1
                if s[l] in tc and windowc[s[l]]<tc[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if reslen!=float("infinity") else ""
