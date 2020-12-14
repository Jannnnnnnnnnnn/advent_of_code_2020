


def product(lst):
    r = 1
    for i in lst:
        r *= i
    return r

def get_sum(inp, sum):
    for i in range(len(inp)):
        for j in range(len(inp)):
            if i == j:
                continue
            
            if inp[i] + inp[j] == sum:
                return f"{inp[i]} + {inp[j]} = {sum}; \n{inp[i]} * {inp[j]} = {inp[i] * inp[j]}"

    print("feller")


def get_sum_3(inp, s):
    for i in inp:
        for j in inp:
            for k in inp:
                if i == j or i == k or j == k:
                    continue
                
                if sum([i, j, k]) == s:
                    return product([i, j, k])

    print("feller")

# def get_sum_recur(inp, s, c, lst):
#     for i in inp:
#         lst.append(i)
#         print(lst, sum(lst))
#         if c > 1:
#             get_sum_recur(inp, s, c-1, lst)

#         elif len(lst) = sum(lst) == s:
#             return product(lst)
#         else: lst.clear()


with open("input.txt", "r") as f:
    inp = [int(i) for i in f.read().split()]

# print(get_sum_recur(inp, 2020, 3, []))
print(get_sum_3(inp, 2020))