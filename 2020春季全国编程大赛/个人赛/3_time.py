class Solution:
    def getTriggerTime(self, increase, requirements):
        result=[-1]*len(requirements)
        C=0
        R=0
        H=0
        count=0
        for i in increase:
            count+=1
            C+=i[0]
            R+=i[1]
            H+=i[2]
            for j in range(len(result)):
                if result[j]!=-1:
                    continue
                if requirements[j][0]==0 and requirements[j][1]==0 and requirements[j][2]==0:
                    result[j]=0
                if requirements[j][0]<=C and requirements[j][1]<=R and requirements[j][2]<=H and result[j]==-1:
                    result[j]=count
        return result
increase = [[1,1,1]]
requirements = [[0,0,0]]

print(Solution().getTriggerTime(increase,requirements))
