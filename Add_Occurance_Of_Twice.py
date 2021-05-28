def main(list1):
    # Write code here
    print(sum(list(filter(lambda i:list1.count(i)==2,set(list1)))))

N = int(input())
Occurance = list(map(int,input().split()))
main(Occurance)
