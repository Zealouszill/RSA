# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

pip install pytest

pytest "filename".py
"""


def ExtendedEuclidianAlgorithm(a, b):

    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b

    return gcd, x, y


def EfficientPowerModAlgorithm(a, b, c):

    power = 1

    a = a % c

    while b > 0:

        if (b & 1) == 1:
           power = (power * a) % c

        b = b >> 1
        a = (a * a) % c

    return power


def EuclideanGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = EuclideanGCD(b % a, a)
        return g, x - (b // a) * y, y


def ModularInverse(a, m):
    g, x, y = EuclideanGCD(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def StrToInt(a):




def test_and():

    assert ModularInverse(3, 4) == 3
    assert ModularInverse(5, 29) == 6
    assert ModularInverse(2, 39) == 20
    assert ModularInverse(3, 25) == 17

    # assert EuclideanGCD(5, 10) == 5



def main():

    a = 110487089277121433970806926710031676468486143869889341376537597422615205558243704080712263653321436167325483283204907700784269778678235765655575460395889011454420593249613544746847538771207567936708769996331073519534473553554551955740383672215173780402123114087748349892379946461583339352705980347602551070771
    b = 111071162799851912824654144483111874424614301938282297067047351983888441559266175769409398076565391663380417335011869271890831362225479632276860946599190038665921626623960557268331733202620352289428928091329109593819133932848528111395029428743390425837597001656830061559982062375737093320355405637563615886803

    print(ExtendedEuclidianAlgorithm(a, b))



main()














