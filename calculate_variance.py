def variance(numbers): 
    mean = sum(numbers)/len(numbers)    
    variance = []
    for x in range(len(numbers)):
        variance.append((numbers[x]-mean)**2)
    final = sum(variance)/len(variance)
    return final
