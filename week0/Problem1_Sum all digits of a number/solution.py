def sum_numbers():
    # getting the file
    file = 'C:/Users/Andre/Desktop/andro.txt'
    #open the file
    openfile = open(file, 'r')
    #reading the file
    content = openfile.read()
    #creating list with all numbers
    nums = content.split(' ')
    #creating variable to add all numbres
    total = 0
    #loop that goes over the list and adds numbres to sum
    
    for i in nums:
       total += int(i)
        
    return total



    

    
