import re


with open("input.txt", "r") as f:
    inp = [ i.split() for i in list(f.readlines())]

for i in range(len(inp)):
    inp[i] = [ int(j) for j in inp[i][0].split("-") ] + [inp[i][1][:-1]] + [inp[i][2]]



def p1_validation(data):
    # total_passwords = len(data)
    valid_passwords = 0
    # invalid_passwords = 0

    for i in data:
        count = len(re.findall(i[2], i[3]))

        if count >= i[0] and count <= i[1]:
            valid_passwords += 1
        # else:
            # invalid_passwords += 1 

    print(valid_passwords)


def p2_validation(data):
    # total_passwords = len(data)
    valid_passwords = 0
    # invalid_passwords = 0

    for i in data:
        if (i[3][i[0]-1] == i[2] or i[3][i[1]-1] == i[2]) and not i[3][i[0]-1] == i[3][i[1]-1]:
            # print(i, i[3][i[0]-1], i[3][i[1]-1])
            valid_passwords += 1
        # else:
            # invalid_passwords += 1 

    print(valid_passwords)

p1_validation(inp)
p2_validation(inp)