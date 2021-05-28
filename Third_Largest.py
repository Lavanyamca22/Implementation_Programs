def main(array):
    # Write code here
    for i in range(2):
        array.remove(max(array))
    print(max(array))


N = int(input())
List = list(map(int,input().split()))
main(List)
