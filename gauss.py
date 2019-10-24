import copy

import numpy

def gaussFunc(a):
    eps = 1e-16

    c = numpy.array(a)
    a = numpy.array(a)

    len1 = 4
    len2 = 5
    vectB = copy.deepcopy(a[:, len1])

    for g in range(len1):

        max = abs(a[g][g])
        my = g
        t1 = g
        while t1 < len1:

            if abs(a[t1][g]) > max:
                max = abs(a[t1][g])
                my = t1
            t1 += 1

        if abs(max) < eps:
            print("Check determinant")

        if my != g:
            b = copy.deepcopy(a[g])
            a[g] = copy.deepcopy(a[my])
            a[my] = copy.deepcopy(b)

        amain = float(a[g][g])

        z = g
        while z < len2:
            a[g][z] = a[g][z] / amain
            z += 1

        j = g + 1

        while j < len1:
            b = a[j][g]
            z = g

            while z < len2:
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1

    a = backTrace(a, len1, len2)

    print("Fallibility:")

    print(vectorN(c, a, len1, vectB))

    return a


def backTrace(a, len1, len2):
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1

        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len2 - 1]


def vectorN(c, a, len1, vectB):
    c = numpy.array(c)
    a = numpy.array(a)
    vectB = numpy.array(vectB)

    b = numpy.zeros((len1))

    i = 0

    while i < len1:
        j = 0
        while j < len1:
            b[i] += c[i][j] * a[j]

            j += 1

        i = i + 1

    c = copy.deepcopy(b)

    for i in range(len1):
        c[i] = abs(c[i] - vectB[i])

    return c

a = numpy.array([[8.3, 2.68, 4.1, 1.9, -10.65],
                 [3.92, 8.45, 7.72  , 2.46, 12.21],
                 [3.77, 7.27, 8.04, 2.28, 15.45],
                 [2.21, 3.59, 1.69, 6.69, -8.35]])

print(a)
print("\n")

b = gaussFunc(a)
print("Answer:")
print(b)
