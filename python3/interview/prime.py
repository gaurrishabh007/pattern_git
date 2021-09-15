# write a program to print prime numbers between 100 to 200

for num in range(100, 200):
    if all(num%i != 0 for i in range (2, num)):
        print(num)
