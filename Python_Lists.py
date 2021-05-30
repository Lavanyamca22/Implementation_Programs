def main():
    # Write code here
    I = []
    Query = int(input())
    for i in range(Query):
        try:
                q,val = input().split(' ')    
                I.append(val)
        except(ValueError):
                print(I)
main()
