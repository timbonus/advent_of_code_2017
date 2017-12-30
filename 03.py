from math import sqrt, pow

with open('03_input.txt','r') as f:
    x = int(f.read())

layer_rough = sqrt(x)
bounding_layers = [0,0]
bounding_layers[0] = int(layer_rough // 1)

if layer_rough == bounding_layers[0]:
    bounding_layers[1] = bounding_layers[0]
    bounding_layers[0] = bounding_layers[1] - 1
else:
    bounding_layers[1] = bounding_layers[0] + 1

def one_pos(bounding_layers):
    if bounding_layers[1] % 2 == 0:
        col = int(bounding_layers[1] / 2 // 1) - 1
        row = int((bounding_layers[1] / 2 // 1))
    else:
        col = int(bounding_layers[1] / 2 // 1)
        row = int((bounding_layers[1] / 2 // 1))
    return (row, col)

def layer_pos(bounding_layers,number):
    corners = [0,0,0]
    corners[0] = int(pow(bounding_layers[0],2) + 1)
    corners[2] = int(pow(bounding_layers[1],2))
    corners[1] = int((corners[0] + corners[2]) / 2)

    if number >= corners[1]:
        if bounding_layers[1] % 2 == 0:
            row = 0
            col = corners[2] - number
        else:
            row = bounding_layers[1] - 1
            col = number  - corners[1]
    else:
        if bounding_layers[1] % 2 == 0:
            col = bounding_layers[1] - 1
            row = corners[1] - number
        else:
            col = 0
            row = number  - corners[0]

    return (row,col)

one_row, one_col = one_pos(bounding_layers)
num_row, num_col = layer_pos(bounding_layers,x)

print(one_row, one_col)
print(num_row, num_col)

print(abs(one_row-num_row) + abs(one_col-num_col))
