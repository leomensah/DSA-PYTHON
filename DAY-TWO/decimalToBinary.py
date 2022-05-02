def decimalToBinary(decimal, result):
    if decimal == 0:
        return result
    result = str(decimal % 2) + result
    return decimalToBinary(decimal // 2, result)

print(decimalToBinary(233, ""))