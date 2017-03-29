#! c:\python27\
import math

def AP(TrueList, PredictList):
    if len(TrueList) != len(PredictList):
        return
    KeyList = []
    for i in range(len(TrueList)):
        KeyList.append((PredictList[i],TrueList[i]))
    KeyList.sort(key = lambda x:-x[0])
    pNum = len(KeyList)
    curRelated = 0
    totalPatK = 0.0
    for i in range(pNum):
        if KeyList[i][1] >= 1:#1,2 are right, 0 is not
            curRelated += 1
            totalPatK += (float)(curRelated)/(i+1)
    totalPatK /= curRelated
    return totalPatK

def MAP(QueryList):
    listNum = len(QueryList)
    if listNum == 0:
        return 0
    meanAP = 0
    for TrueList, PredictList in QueryList:
        meanAP += AP(TrueList, PredictList)
    return meanAP/listNum

def DCG(PredictList, n):
    if len(PredictList) < n:
        return
    result = 0
    for i in range(n):
        result += (pow(2, PredictList[i])-1)/math.log(2+i, 2)
    return result

def NDCG(TrueList, PredictList, n):
    if len(TrueList) != len(PredictList):
        return
    if len(TrueList) < n:
        return
    tmpList = TrueList
    tmpList.sort()
    tmpList.reverse()
    bestdcg = DCG(tmpList, n)
    KeyList = []
    for i in range(len(TrueList)):
        KeyList.append((PredictList[i],TrueList[i]))
    KeyList.sort(key = lambda x:-x[0])
    tmpList = []
    for i in range(len(KeyList)):
        tmpList.append(KeyList[i][1])
    dcg = DCG(tmpList, n)

    return dcg/bestdcg

#print MAP([1,2,3,4], [0.8,0.5,0.9,0.1])
a = [0,1,2,3]
b = [0.8,0.5,0.9,0.1]

print ('AP is ', AP(a, b))
for i in range(4):
    print ('NDCG is ', NDCG(a, b, i+1))
