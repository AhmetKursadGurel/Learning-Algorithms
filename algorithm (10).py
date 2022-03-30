def creator(lower,higher):
    lower,higher=str(lower),str(higher)
    count=0
    my_initial_list=[]
    if len(lower) == len(higher):
        my_num=""+lower[0]
        count=int(lower[0])
        
        for index in range(len(lower)):
        
            for index in range(len(lower)-1):
                count+=1
                my_num+=str(count)
                my_initial_list.append(my_num)
            
        print(my_initial_list)


creator(100,800) 
