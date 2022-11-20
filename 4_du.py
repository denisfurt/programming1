from heapq import nlargest

numbers = []
newNum = int(input())

while newNum != -1:
    numbers.append(newNum)
    newNum = int(input());

k = int(input())

print(min(nlargest(k, numbers)))
