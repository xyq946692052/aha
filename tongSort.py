def tong(lst):
    maxLen=max(lst)+1
    nLst=[0]*maxLen
    for k in lst:
        nLst[k]+=1
    for i in range(len(nLst)):
        if nLst[i]!=0:
            for k in range(nLst[i]):
                print i,

if __name__=='__main__':
    lst=[1,3,5,6,9,2,3,66,44,9,0,7,11,234,89,31]
    print lst
    tong(lst)
