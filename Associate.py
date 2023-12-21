
class Associate:
    def __init__(self,id1,name,technology,experienceinyear):
        self.id1 = id1
        self.name = name
        self.technology = technology
        self.experienceinyear = experienceinyear
        
class Solution:
    @classmethod
    def associateforgiventechnology(cls,arrAssociate,searchtechnology):
        result = []
        name = ''
        for i in arrAssociate:           
            if i.technology.lower()==searchtechnology.lower() and i.experienceinyear %5 == 0:
                result.append(i.id1)
                name = i.name
                #print(name)
        return result
        return name
            

n = int(input())
arrAssociate = []
for i in range(n):
    id1 = int(input())
    name = input()
    technology = input()
    experienceinyear = int(input())

    arrAssociate.append(Associate(id1,name,technology,experienceinyear))

searchtechnology = input()

ans = Solution.associateforgiventechnology(arrAssociate,searchtechnology)
#ans1 = Solution.associateforgiventechnology(arrAssociate,searchtechnology)

for i in ans: 
    print(i)


