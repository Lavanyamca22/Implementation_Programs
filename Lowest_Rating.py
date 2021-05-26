N = int(input())
mem = [[input(),int(input())] for i in range(N)]
Num =[mem[i][1] for i in range(0,len(mem))]
if(Num.count(min(Num))==1):
    print(mem[Num.index(min(Num))][0])
else:
    print(*sorted([mem[i][0] for i in range(0,len(Num)) if(Num[i] == min(Num))]),sep='\n')
