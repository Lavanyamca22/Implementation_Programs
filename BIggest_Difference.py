def main(Difference):
    # Write code here
    print(max(Difference)-min(Difference)) 

N = int(input())
Diff = list(map(int,input().split()))
main(Diff)
