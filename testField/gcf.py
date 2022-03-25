def gcf(c, k):
    n = (c, k)
    c = max(n)
    k = min(n)
    r = c % k
    if r != 0:
        # print(r)
        return gcf(k, r)
    return k


print(gcf(85489656465148796515498654998654, 545468745619841897654987486832))
