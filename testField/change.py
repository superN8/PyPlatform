def change(p):
    q = int(p / 25)
    p -= (q * 25)
    d = int(p / 10)
    p -= (d * 10)
    n = int(p / 5)
    p -= (n * 5)
    return [q, d, n, p]
