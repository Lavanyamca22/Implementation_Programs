def main(C):
    # Write code here
    result = 0
    for i in C:
        if(C.count(i)==1):
            result +=1
    print(result)
N = int(input())
Cities = [input() for i in range(N)]
main(Cities)
