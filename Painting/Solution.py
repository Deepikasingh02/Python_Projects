
class Painting:
    def __init__(self,paintingid, painterName,paintingprice,paintingtype):
        self.paintingid = paintingid
        self.painterName = painterName
        self.paintingprice = paintingprice
        self.paintingtype = paintingtype

class ShowRoom:
    #def __init__ (self, paintingList):
       # self.paintingList = paintingList

        
    def getTotalPaintingPrice (findingtype , list_obj):
        result = 0
        flag = 0
        for i in list_obj:
            result+=1
            flag = 1
        if flag ==0:
            return "No painting found"
        else:
            return result

    def getPaintingWithMaxCountofPrice(list_obj):
        d= {}
        s =0
        for i in list_obj:
            if i.painterName in d.key():
                d[i.painterName] += 1
            else:
                d[i.painterName] = 1
        for i in sorted(d.key()):
            if s <d[i]:
                s = d[i]
                name = i
        return name
            


n = int(input())
list_obj = []
for i in range(n):
    paintingid = input()
    painterName = input()
    paintingprice = int(input())
    paintingtype = input()

    list_obj.append(Painting(paintingid, painterName,paintingprice,paintingtype))

findingtype = input()
        #paint = ShowRoom(list_obj)

ans1 = ShowRoom.getTotalPaintingPrice(findingtype , list_obj)
ans2 = ShowRoom.getTotalPaintingPrice(list_obj) 
print(ans1)
print(ans2)




    
