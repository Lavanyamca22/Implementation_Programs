
def main(List):
    # Write code here
    if(len(list(filter(lambda i:int(i)%2!=0,List))) == 0):
        print(0)
    else:
        Odd = (list(filter(lambda i:i%2!=0,List)))
        Odd.sort(reverse=True)
        print(''.join(list(map(str,Odd))))

N = int(input())
List = list(map(int,input().split()))
main(List)
