#Without Function
def main(Strings):
  n = [ord(i[0]) for i in Strings]
  m = n.copy()
  while m != []:
    minimum = min(m)
    index = n.index(minimum)
    result.append(Strings[index])
    m.remove(min(m))
    return result

#With Function
def main(Strings):
    # Write code here
    Strings.sort()
    for i in Strings:
        print(i)

N = int(input())
Strings = [input() for i in range(N)]
main(Strings)
