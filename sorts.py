def insertion(x,time):
    
    start = time()
    
    for i in range(1, len(x)):
        
        key = x[i]
        j = i-1
        while j >=0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key    
    
    end = time()
    
    print("Time for insertion sorting is:", end - start, "\n")
    return x