def quickSort(lst,left,right):
    if left>right:
        return

    tmp=lst[left]
    i=left
    j=right

    while i!=j:
        while lst[j]<=tmp and j>i:
            j-=1
        lst[i]=lst[j]
        while lst[i]>=tmp and j>i:
            i+=1
        lst[j]=lst[i]

    lst[i]=tmp
    quickSort(lst,left,i-1)
    quickSort(lst,i+1,right)
     
    return lst   

if __name__=='__main__':
    lst=[12,4,3,4,4,234,53461241,1134,4,5,6,1,0,11,2,9,7,3]
    print lst
    quickSort(lst,0,len(lst)-1)
    print lst[::-1]
    
        
        
    
