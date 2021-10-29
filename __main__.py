import random


def find_LCS(S, T):
    n = len(S)
    m = len(T)
    r = [[0 for x in range(m + 1)] for y in range(n + 1)]
    p = [['' for x in range(m + 1)] for y in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                r[i][j] = r[i - 1][j - 1] + 1
                p[i][j] = 'lt'
            elif r[i - 1][j] >= r[i][j - 1]:
                r[i][j] = r[i - 1][j]
                p[i][j] = 't'
            else:
                r[i][j] = r[i][j - 1]
                p[i][j] = 'l'
    return r, p


def PRINT_LCS(p, S, i, j, res):
    if i == 0 or j == 0:
        return
    if p[i][j] == "lt":
        PRINT_LCS(p, S, i - 1, j - 1, res)
        res = res.append(S[i - 1])
    elif p[i][j] == "t":
        PRINT_LCS(p, S, i - 1, j, res)
    else:
        PRINT_LCS(p, S, i, j - 1, res)


def LCS(S, T):
    r, p = find_LCS(S, T)
    res = []
    PRINT_LCS(p, S, len(S), len(T), res)
    return res


def __main__():
    S = [random.randint(0,10) for x in range(random.randint(10,20))]
    T = [random.randint(0, 10) for x in range(random.randint(10, 20))]
    print("S=",S)
    print("T=",T)
    # e.g 1:
    # Output the LCS of S and T
    print("LCS(S,T)=",LCS(S, T))

    # e.g 2:
    # Output the longest increasing subsequence(LIS) of S
    print("LIS(S)=",LCS(S, sorted(S)))


if __name__ == "__main__":
    __main__()
