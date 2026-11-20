for i in range(5):
    for j in range(5-i):# j will print the value of 5-i for each iteration of j,resulting in a triangle pattern where each row 
   #contains the same number of spaces as the row number strating from 0to4
        print(" ",end=" ")
    for k in range(i):#k will print the value of i for each iteration of k,resulting in a triangle pattern where
     # each row contains the same number of *as the row number strating from 0 to 4
        print("*",end=" ")
    print()