def main(n):
    # Write code here 
    list1 = list(map(int,input().split()))
    print('{:.3f}'.format(sum(list1)/len(list1)))
n = int(input())
main(n)
