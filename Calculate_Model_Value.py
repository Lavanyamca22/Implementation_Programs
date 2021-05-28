from collections import Counter
def main(list1):
    # Write code here
    Count = Counter(list1)
    print(list(Count.keys())[list(Count.values()).index(max(Count.values()))])

N = int(input())
Model_value_array = list(map(int,input().split()))
main(Model_value_array)
