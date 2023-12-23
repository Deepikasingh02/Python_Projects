class CricketPlayer:
    def __init__(self,CplayerNmae,cplayerCountry,cplayerAge,cpCountryFrom):
        self.CplayerNmae = CplayerNmae
        self.cplayerCountry = cplayerCountry
        self.cplayerAge = cplayerAge
        self.cpCountryFrom = cpCountryFrom

class Solution:
    def countPlayer(countryName,list_obj):
        counter = 0
        for i in list_obj:
            if countryName.lower() == i.cpCountryFrom.lower():
                counter += 1
        return counter
    def getPlayerPlayedForMaxCountry (list_obj):
        max_count = 0
        max_name = ''
        for i in list_obj:
            list1 = i.cplayerCountry
            if max_count < len(list1):
                max_count = len(list1)
                max_name = i.CplayerNmae
        return max_name        


n = int(input())
list_obj = []
for i in range(n):
    CplayerNmae = input()
    c= int(input())
    cplayerCountry = []
    for j in range(c):
        cplayerCountry.append(input())
    cplayerAge = int(input())
    cpCountryFrom = input()


    list_obj.append(CricketPlayer(CplayerNmae,cplayerCountry,cplayerAge,cpCountryFrom))

countryName = input()

ans1 = Solution.countPlayer(countryName,list_obj)
ans2 = Solution.getPlayerPlayedForMaxCountry(list_obj)

print(ans1)
print(ans2) 

    
