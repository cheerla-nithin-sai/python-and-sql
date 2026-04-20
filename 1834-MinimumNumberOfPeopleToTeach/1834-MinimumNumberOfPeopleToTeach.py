# Last updated: 4/20/2026, 1:25:56 PM
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cnt={}
        users=set()
        for u,v in friendships:
            u=u-1
            v=v-1
            common=False
            for lan in languages[u]:
                if lan in languages[v]:
                    common=True
                    break
            if not common:
                users.add(u)
                users.add(v)
        if not users:
            return 0
        lan_dict=Counter()
        for user in users:
            for lan in languages[user]:
                lan_dict[lan]+=1
        return len(users)-max(lan_dict.values())
            



            
        