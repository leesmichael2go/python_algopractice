#https://www.hackerrank.com/challenges/staircase
steps = int(input())
i = 1
while i <= steps:
    blanks = [" "] * (steps - i)
    bricks = ["#"] * i
    line = blanks + bricks
    print(''.join(line))
    i += 1