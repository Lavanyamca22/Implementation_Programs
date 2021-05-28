def main(List):
    # Write code here
    if(len(list(filter(lambda i:int(i)%2==0,List))) == 0):
        print(0)
    else:
        print(''.join(list(filter(lambda i:int(i)%2==0,List))))

N = int(input())
List = list(map(str,input().split()))
main(List)
