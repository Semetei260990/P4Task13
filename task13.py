def superDigit(n, k):
    m = n * k

    while True:
        m = sum(list(map(int, m)))
        m = str(m)
        if len(m) == 1:
            return m
            break