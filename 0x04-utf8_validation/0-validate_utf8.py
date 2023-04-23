#!/usr/bin/python3
'''UTF-8 Validation'''


def startsWith10(binary_strs):
    '''checks if binary form starts with 10'''
    res = True
    for element in binary_strs:
        if (not(element.startswith('10'))):
            res = False
            break
    return res


def convertToBinary(num):
    '''converts int to binary form and returns
    the 8 list significant bits'''
    binary_form = '{:08b}'.format(num)
    if (len(binary_form) > 8):
        binary_form = binary_form[-8:]
    return binary_form


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding'''
    isValid = True
    for i in range(len(data)):
        binary_form = convertToBinary(data[i])
        # print("bin: {}, dec: {}".format(binary_form, data[i]))
        if (binary_form.startswith('0')):
            continue
        elif (binary_form.startswith('110')):
            # print("2:byte")
            if (i + 1 < len(data)):
                next_byte = convertToBinary(data[i+1])
                # print(next_byte)
                if (startsWith10([next_byte])):
                    i = i + 1
                else:
                    return False
            else:
                return False
        elif (binary_form.startswith('1110')):
            # print("3:byte")
            if (i + 2 < len(data)):
                next_byte1 = convertToBinary(data[i+1])
                next_byte2 = convertToBinary(data[i+2])
                # print(next_byte1, next_byte2)
                if (startsWith10([next_byte1, next_byte2])):
                    i = i + 2
                else:
                    return False
            else:
                return False
        elif (binary_form.startswith('11110')):
            # print("4:byte")
            if (i + 3 < len(data)):
                next_byte = convertToBinary(data[i+1])
                next_byte1 = convertToBinary(data[i+2])
                next_byte2 = convertToBinary(data[i+3])
                if (startsWith10([next_byte, next_byte1, next_byte2])):
                    i = i + 3
                else:
                    return False
            else:
                return False
        elif (binary_form.startswith('10')):
            return False
    return isValid
