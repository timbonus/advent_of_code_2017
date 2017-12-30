with open('02_input.txt','r') as f:
    x = f.read()

x_rows = x.split('\n')
x_arr = [[int(n) for n in row.split()] for row in x_rows if len(row) > 0]
x_minmax = [(max(row) - min(row)) for row in x_arr]

print(sum(x_minmax))
