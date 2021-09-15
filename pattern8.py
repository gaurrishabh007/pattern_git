n=int(input("enter no of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(100+n-i), end=" ")
    print()