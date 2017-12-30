with open('01_input.txt','r') as f:
    x = f.read()

if x[0] == x[-1]:
    cumsum = int(x[0])
else:
    cumsum = 0

last = x[0]

for i in x:
    if i == last:
        cumsum += int(i)
    last = i

print(cumsum)
