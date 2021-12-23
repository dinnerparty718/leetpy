cell = (0, 0)
d = 0
i, j = cell
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


for idx, new_cell in enumerate([(i-1, j), (i, j+1), (i+1, j), (i, j-1)]):
    new_d = (d + idx) % 4
    print(new_d, new_cell)

print('')

for i in range(4):
    new_d = (d + i) % 4  # new_d 0,1,2,3
    new_cell = (cell[0] + directions[new_d][0],
                cell[1] + directions[new_d][1])

    print(new_d, new_cell)
