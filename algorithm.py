input_list=[1,2,3,4,5,2,3,4,5,3,4,5,4,5,5,4]
def freq(my_list):
    
    
    bye_list=list(set(my_list))
    value_list=[]
    index_list=[]
    """print(bye_list)"""
    for index in bye_list:
        
        count = 0
        for element in my_list:
            
            if int(element) == int(index):

                count+=1
        value_list.append(count)
        """print(f"{index} => {count}")"""
        

    """print(value_list)"""

    def maxelements(seq):
        max_indices = []
        if seq:
            max_val = seq[0]
            for i,val in ((i,val) for i,val in enumerate(seq) if val >= max_val):
                if val == max_val:
                    max_indices.append(i)
                else:
                    max_val = val
                    max_indices = [i]

        return max_indices
    duplicate_index  = maxelements(value_list)
    for smt in duplicate_index:
        index_list.append(smt)
    final_list=[]
    for q in index_list:
        final_list.append(bye_list[q])
    """print(final_list)"""
    if len(final_list)==1:
        return(final_list[0],max(value_list))
    else:
        return(final_list,max(value_list))

    

        

    
    
    

print(freq(input_list))

