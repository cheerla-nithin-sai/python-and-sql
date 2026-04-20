# Last updated: 4/20/2026, 1:25:59 PM
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def rem_substr(s,first,sec,points):
            score=0
            st=[]
            for char in s:
                if st and st[-1]==first and char==sec :
                    score+=points
                    st.pop()
                else:
                    st.append(char)
            return "".join(st),score
        if x>y:
            s,score1=rem_substr(s,'a','b',x)
            s,score2=rem_substr(s,'b','a',y)
        else:
            s,score1=rem_substr(s,'b','a',y)
            s,score2=rem_substr(s,'a','b',x)
        return score1+score2