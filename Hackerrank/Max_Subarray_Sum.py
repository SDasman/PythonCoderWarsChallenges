def maximumSum(a, m):
    sub_arrays = [[]] 
    current_max = 0
    # first loop  
    for i in range(len(a) + 1): 
        # second loop  
        for j in range(i + 1, len(a) + 1):  
            # slice the sublist
            sub = a[i:j] 
            sub_list_m = (sum(sub))%m
            if sub_list_m > current_max:
                current_max = sub_list_m        
    return current_max
