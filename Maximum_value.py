#Without using any functions
def main(n):
    # Write code here
    list1 = [int(input()) for i in range(n)]
    maximum = 0
    for i in list1:
        if i>maximum:
            maximum = i 
    print(maximum)

n = int(input())
main(n)

#Using function
def main(n):
    # Write code here
    list1 = [int(input()) for i in range(n)]
    print(max(list1)

n = int(input())
main(n)
