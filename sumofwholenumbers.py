#input an integer value

n= int(input("enter the numbers you want to find:"))
sum=0

#iterates for n+1 times: i=1 to n+1
for i in range(1, n+1):
    sum=sum+1
    print("\nSum=", sum)