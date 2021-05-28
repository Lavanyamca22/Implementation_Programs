def main(array):
    # Write code here
    Even = list(filter(lambda i:i%2==0,array))
    Odd = list(filter(lambda i:i%2!=0,array))
    if(sum(Even)>sum(Odd)):
        print("Even")
    elif(sum(Even)<sum(Odd)):
        print("Odd")
    elif(sum(Even)==sum(Odd)):
        print("Tied") 

N = int(input())
war= list(map(int,input().split()))
main(war)
