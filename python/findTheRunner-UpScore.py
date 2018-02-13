n = int(input())
arr = map(int, input().split())

first = int(-100)
second = int(-100)

for x in arr:
  if (x > first):
    second = first
    first = x
  if (x < first and x > second):
    second = x
  

print(second)
  