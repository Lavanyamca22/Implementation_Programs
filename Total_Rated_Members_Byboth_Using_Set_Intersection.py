def main(a,b):
    # Write code here
    print(len(a.intersection(b)))
A = int(input())
List_A = set(map(int,input().split()))
B = int(input())
List_B = set(map(int,input().split()))
main(List_A,List_B)
