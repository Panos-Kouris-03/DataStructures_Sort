def selection(x,time):
    
    start = time()

    for i in range(len(x)):
        min=i
        for j in range(i+1,len()):
            if x[min] > x[j]:
                min = j
        x[i], x[min] = x[min], x[i]
            
    end = time()
    print("Time for selection sort:",end-start, "\n")
    return min