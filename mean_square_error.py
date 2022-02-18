def solution(array_a, array_b):
    diffA = []
    for x in range(len(array_a)):
        diffA.append(abs(array_a[x]-array_b[x]))
    diffA = list(map(lambda x : x**2,diffA))
    final = sum(diffA)/len(diffA)
    return final
