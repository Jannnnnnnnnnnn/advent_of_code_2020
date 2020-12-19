import math

with open("input.txt", "r") as f:
    inp = [i.split("\n")[0] for i in f.readlines()]




def check_trees(movement):
    line_len = len(inp[0])
    trees = 0
    cord_x = 0
    cord_y = 0
    while cord_y < len(inp):
        if inp[cord_y][cord_x%line_len] == "#":
            trees += 1
        cord_y += movement[1]
        cord_x += movement[0]
        
    print(movement, trees)
    return trees


product = 1
product *= check_trees([1, 1])
product *= check_trees([3, 1])
product *= check_trees([5, 1])
product *= check_trees([7, 1])
product *= check_trees([1, 2])

print(product)