s = '1kl68k'
sum = 0
for x in s:
    if x.isnumeric():
        sum = sum + int(x)
print(sum)

