import time


def primise(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = []
    for i in range(3, n + 1):
        if i % 2 != 0:
            s.append(i)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = int((m * m - 3) / 2)
            s[j] = 0
            while j < half:
                s[j - 1] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    l = [2]
    for x in s:
        if x:
            l.append(x)
    return l


def primise2(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = list(range(3, n + 1, 2))
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = int((m * m - 3) / 2)
            s[j] = 0
            while j < half:
                s[j - 1] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    l = [2] + [x for x in s if x]
    return l


def benchmark():
    start = time.time()
    for _ in range(40):
        count = len(primise(10000))
    end = time.time()
    print("benchmark duration: %r seconds" % (end - start))
    print(count)


if __name__=="__main__":
    benchmark()
