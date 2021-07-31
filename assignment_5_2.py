largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        cnum=int(num)
    except:
        print('Invalid input')
        #print (smallest,largest)
    
    
    if smallest == None:
        smallest =cnum
        largest = cnum
    elif cnum < smallest :
        smallest = cnum
    elif cnum > largest:
        largest=cnum
        
    
    
print("Maximum", largest)
print("Minimum", smallest)
    
    

