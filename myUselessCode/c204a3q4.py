def qsort(list, start, end): 
    print start,end
    if start < end:
        print list
        split = pn(list, start, end) 
        qsort(list, start, split-1) 
        qsort(list, split+1, end)
    else: 
        print ''

def pn(list,start,end):
    pivot = list[start]    # partition around the last value
    tl=[]
    tm=[]
    for index in (range(start+1,end+1)):
#        print start,end,index
        if list[index]>pivot:
            tm.append(list[index])
        else:
            tl.append(list[index])
    t=tl+[pivot]+tm
#    print t
    list[start:end+1]=t
    split=len(tl)+start
#    print 'p'
#    print list
    return split

L = [44,88,11,0,33,99,22,77,66,55] 
qsort(L,0,len(L)-1)
