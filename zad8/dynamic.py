from timeit import default_timer as timer

def P_rec(i, j):
    if i == 0.0 and j == 0.0:
        return 0.5
    if i > 0.0 and j == 0.0:
        return 0.0
    if i == 0.0 and j > 0.0:
        return 1.0
    if i > 0.0 and j > 0.0:
        return 0.5 * (P_rec(i - 1.0, j) + P_rec(i, j - 1))


dict = {(0, 0): 0.5, (1, 0): 0, (0, 1): 1}

def P_dyn(i, j):
    if((i, j) in dict):
        return dict.get((i, j))
    elif (i == 0 and j > 0):
        return 1
    elif (i > 0 and j == 0):
        return 0
    else:
        x = 0.5 * (P_dyn(i, j - 1) + P_dyn(i - 1, j))
        dict[(i, j)] = x
        return x

P_dyn(1, 3)
P_dyn(2, 2)

start = timer()
P_dyn(10, 10)
end = timer()
print("Dynamicznie: ", end - start)

start = timer()
P_rec(10, 10)
end = timer()
print("Rekurencyjnie: ", end - start)
