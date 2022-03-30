def listReplace(list1,tuple1,tuple2):
    for i in range(0,len(list1)):
        x=int(i)
        a=tuple1[0]
        b=tuple1[1]
        c=tuple2[0]
        d=tuple2[1]
        if list1[x]==a:
            list1[x]=b
        elif list1[x]==c:
            list1[x]=d
    
    return list1



        
        
        
        





