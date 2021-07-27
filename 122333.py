                #         1
                #       2 2 
                #     3 3 3
                #   4 4 4 4 
                # 5 5 5 5 5 


i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end=" ")
        j=j+1
    c=1
    while c<=i:
        print(i,end=" ") 
        c=c+1
    print()
    i=i+1