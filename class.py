st="greekyshows"
for i in st:
    print(i)
    # nested for loop 
    for i in range (2):
        print("outer loop",i)
        for j in range (3):
            print("inner loop",j)