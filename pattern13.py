n=int(input("enter number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(60+i), end=" ")
    print()