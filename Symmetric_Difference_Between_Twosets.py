def main(A,B):
    # Write code here
    for i in (A-B).union(B-A):
        print(i)

setA = int(input())
setA_ele = set(map(int,input().split()))
setB = int(input())
setB_ele = set(map(int,input().split()))
main(setA_ele,setB_ele)
