# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

pip install pytest

pytest "filename".py
"""


def ExtendedEuclidianAlgorithm(a, b):

    """
    returns a single character '0'
    representing a logical AND of
    bit a and bit b (which are each 0 or 1

    >>> AND('0', '1')
    '0'
    >>> AND('1', '1')
    '1'
    """

    if (a == '1'):
        if (b == '1'):
            return '1'
        else:
            return '0'
    else:
        return '0'


def test_and():

    assert ExtendedEuclidianAlgorithm('0', '0') == '0'
    assert ExtendedEuclidianAlgorithm('0', '1') == '0'
    assert ExtendedEuclidianAlgorithm('1', '0') == '0'
    assert ExtendedEuclidianAlgorithm('1', '1') == '1'
















