ppList = ["a", "c", "b", "g", "i", "u" , "h", "z", "y"]

for i in range(1, len(ppList)): 
    key = ppList[i] 
    j = i-1
    while j >=0 and key < ppList[j] : 
            ppList[j+1] = ppList[j] 
            j -= 1
    ppList[j+1] = key

print(ppList)