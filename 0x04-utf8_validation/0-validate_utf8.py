#!/usr/bin/python3
'''UTF-8 Validation'''


def convertToBinary(num):
    '''converts int to binary form and returns
    the 8 list significant bits'''
    binary_form = '{:08b}'.format(num)
    if (len(binary_form) > 8):
        binary_form = binary_form[-8:]
    return binary_form


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding'''
    start_byte = True
    trailing_bytes = 0
    for num in data:
        binary = convertToBinary(num)
        if start_byte:
            if binary.startswith('10'):
                return False
            elif binary.startswith('110'):
                trailing_bytes = 1
                start_byte = False
            elif binary.startswith('1110'):
                trailing_bytes = 2
                start_byte = False
            elif binary.startswith('11110'):
                trailing_bytes = 3
                start_byte = False
        else:
            if not binary.startswith('10'):
                return False
            trailing_bytes -= 1
            if (trailing_bytes < 0):
                return False
            if (trailing_bytes == 0):
                start_byte = True
    return True
