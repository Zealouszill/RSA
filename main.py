# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

pip install pytest

pytest "filename".py



def ExtendedEuclidianAlgorithm(firstNumber, secondNumber):
    x, y, u, v = 0, 1, 1, 0

    while firstNumber != 0:
        quotient, remainder = secondNumber // firstNumber, secondNumber % firstNumber
        m, n = x - u * quotient, y - v * quotient
        trash1, trash2, x, y, u, v = firstNumber, remainder, u, v, m, n

    GCD = secondNumber

    return GCD, x, y
"""

def EfficientPowerModAlgorithm(base, power, mod):
    powerTemp = 1

    base = base % mod

    while power > 0:

        if (power & 1) == 1:
            powerTemp = (powerTemp * base) % mod

        power = power >> 1
        base = (base * base) % mod

    return powerTemp


def EfficientPowerModAlgRecur(base, power, mod):

    if power == 0:
        return 1

    partial = EfficientPowerModAlgRecur(base, power // 2, mod)

    if power % 2 == 0:
        return partial * partial % mod

    else:
        return partial * partial * base % mod



def EuclideanGCD(firstNumber, secondNumber):

    # Make sure that the left number is bigger than the other.

    # Base case. If firstNumber is zero, return the second number as the GCD
    if firstNumber == 0:
        return secondNumber, 0, 1

    # Recursion. If the number can be divided by the second number, then do so.
    else:
        GCD, y, x = EuclideanGCD(secondNumber % firstNumber, firstNumber)
        return GCD, x - (secondNumber // firstNumber) * y, y


# A * B mod C for B values 0 through C-1
def ModularInverse(firstNumber, secondNumber):
    result, x, trash2 = EuclideanGCD(firstNumber, secondNumber)

    if result != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % secondNumber


def convertStringToInteger(stringList):
    intList = [int(s) for s in stringList.split(' ')]
    return intList


def convertIntegerToString(intList):
    return " ".join(map(str, intList))

def makingPrivateNandD(p, q, e):

    return p*q, ModularInverse(e, (p-1)*(q-1))

def encrypt(xMessage, N, e):
    """
    returns the encrypted 'y' using the public of N,e.

    y = (x^e mod N)
    """

    # return xMessage**e % N

    return EfficientPowerModAlgorithm(base=xMessage, power=e, mod=N)

def decryptMessage(encryptedMessage, N, d):
    """
    returns the decrypted message 'x' using the private of N,d.

    N = product of two prime numbers

    x = (y^d mod N)
    """

    # return encryptedMessage**d % N

    return EfficientPowerModAlgorithm(base=encryptedMessage, power=d, mod=N)


def test_makingPrivatesDN():

    assert makingPrivateNandD(p = 5, q = 11, e = 3) == (55, 27)

def test_allTheFunctions():

    p = 110487089277121433970806926710031676468486143869889341376537597422615205558243704080712263653321436167325483283204907700784269778678235765655575460395889011454420593249613544746847538771207567936708769996331073519534473553554551955740383672215173780402123114087748349892379946461583339352705980347602551070771
    q = 111071162799851912824654144483111874424614301938282297067047351983888441559266175769409398076565391663380417335011869271890831362225479632276860946599190038665921626623960557268331733202620352289428928091329109593819133932848528111395029428743390425837597001656830061559982062375737093320355405637563615886803
    e = 121497340871047561990526349313922431040502436205277029161504074265656522318180600371526800734743195781676485261271407335077142141062183325700299129778874273734144338622599487090131017655398226759216026150060144849693132978936886491999493651200251158512013123761065143321228864622882636292486361150032268778811

    numMessage = 15879465132165498446513216546874695132165346549685163213516351

    textMessage = "This is a message"


    #p = 31
    #q = 57
    #e = 101

    N, d = makingPrivateNandD(p, q, e)

    encryptedMessaged = encrypt(message, N, e)

    decryptedMessage = decryptMessage(encryptedMessaged, N, d)

    assert e*d % ((p-1)*(q-1)) == 1

    assert decryptedMessage == textMessage

def test_encrypt():

    assert encrypt(xMessage=13, e=3, N=55) == 52

def test_decrypt():

    assert decryptMessage(encryptedMessage=52, d=27, N=55) == 13

def test_EGCD():

    assert EuclideanGCD(5, 10) == (5, 1, 0)
    assert EuclideanGCD(27, 13) == (1, 1, -2)
    assert EuclideanGCD(105, 15) == (15, 0, 1)

    assert EuclideanGCD(10, 5) == (5, 0, 1)
    assert EuclideanGCD(1, 213) == (1, 1, 0)

def test_PowerAlg():

    assert EfficientPowerModAlgorithm(35, 78, 22) == (35**78 % 22)
    assert EfficientPowerModAlgorithm(13, 3, 55) == (13 ** 3 % 55)
    assert EfficientPowerModAlgorithm(13, 3, 55) == 52

def test_PowerAlgRecur():

    assert EfficientPowerModAlgRecur(13, 3, 55) == 52
    assert EfficientPowerModAlgRecur(35, 78, 22) == (35**78 % 22)
    assert EfficientPowerModAlgRecur(13, 3, 55) == (13 ** 3 % 55)

def test_ExtendedEuclidianAlgorithm():

    pass
    #assert ExtendedEuclidianAlgorithm(5, 10) == (5, 1, 0)
    #assert ExtendedEuclidianAlgorithm(27, 13) == (1, 1, -2)
    #assert ExtendedEuclidianAlgorithm(105, 15) == (15, 0, 1)

def test_ModularInverse():

    assert ModularInverse(7, 3) == 1
    assert ModularInverse(3, 4) == 3
    assert ModularInverse(5, 29) == 6
    assert ModularInverse(2, 39) == 20
    assert ModularInverse(3, 25) == 17


def test_strings():

    assert convertStringToInteger('0 1 2 3 4 5 6 7 8 9') == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert convertIntegerToString([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == '0 1 2 3 4 5 6 7 8 9'

# if __name__ == "__main__":
