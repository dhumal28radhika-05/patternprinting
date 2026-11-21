for i in range(5,0,-1):# the outer loop is used to print the number of rows 
    for j in range(5-i):# the inner loop is used to print the spaces before the stars in each row
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()