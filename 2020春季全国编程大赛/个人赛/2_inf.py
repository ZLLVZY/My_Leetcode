class Solution:
    def numWays(self,n,relation,k):
        result=0
        if k==1:
            for i in relation:
                if i[0]==0 and i[1]==n-1:
                    result+=1
        elif k==2:
            for i in relation:
                if i[0]==0:
                    for j in relation:
                        if j[0]==i[1] and j[1]==n-1:
                            result+=1
        elif k==3:
            for i in relation:
                if i[0]==0:
                    for j in relation:
                        if j[0]==i[1]:
                            for v in relation:
                                if v[0]==j[1] and v[1]==n-1:
                                    result+=1
        elif k==4:
            for i in relation:
                if i[0]==0:
                    for j in relation:
                        if j[0]==i[1]:
                            for v in relation:
                                if v[0]==j[1]:
                                    for m in relation:
                                        if m[0]==v[1] and m[1]==n-1:
                                            result+=1
        elif k==5:
            for i in relation:
                if i[0]==0:
                    for j in relation:
                        if j[0]==i[1]:
                            for v in relation:
                                if v[0]==j[1]:
                                    for m in relation:
                                        if m[0]==v[1]:
                                            for b in relation:
                                                if b[0]==m[1] and b[1]==n-1:
                                                    result+=1
        return result

n=3
relation=[[0,2],[2,1]]
k=2
print(Solution().numWays(n,relation,k))

