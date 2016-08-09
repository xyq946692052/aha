def maopao(lst):
     for i in range(len(lst)-1):
         for j in range(len(lst)-1):
             if lst[j]>lst[j+1]:
                 lst[j],lst[j+1]=lst[j+1],lst[j]
     print lst
     

if __name__=='__main__':
    lst=[1,3,5,8,2,11,6,4,0,3,6,51,23,7,9]
    print lst
    maopao(lst)
