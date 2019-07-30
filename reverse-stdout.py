import sys

text = sys.stdin.read()
lines = text.splitlines()

for line in lines:
    words = line.split()
    for word in words:
        print(word[::-1], end=" ")
    print("\n")