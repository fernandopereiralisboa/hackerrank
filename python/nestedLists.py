n = int(input())
students = [[input(), float(input())] for _ in range(n)]

secondLowest = sorted(list(set([student for name, student in students])))[1]

print('\n'.join([a for a,b in sorted(students) if b == second_highest]))