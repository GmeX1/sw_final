import sys

data = list(map(str.strip, list(sys.stdin)))
stars = list(data.pop(0))
out = list()
for string in data:
    min_len = float('inf')
    for i in range(len(string)):
        if string[i] in stars:
            count = 0
            for j in range(i + 1, len(string)):
                if string[j] in stars:
                    count += 1
                if count == 2:
                    min_len = min(min_len, j - i + 1)
                    break
    if min_len != float('inf'):
        out.append(min_len)
print(' '.join(map(str, out)))
