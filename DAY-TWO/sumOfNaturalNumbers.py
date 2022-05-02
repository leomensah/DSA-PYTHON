def sumNaturalNumbers(inputNumber, result):
    if inputNumber == 0:
        return result
    result = (inputNumber) + result
    return sumNaturalNumbers(inputNumber-1, result)

def sumNaturalNumbers_Alpha(inputNumber):
    if inputNumber <= 1:
        return inputNumber
    return inputNumber + sumNaturalNumbers_Alpha(inputNumber-1)

print(sumNaturalNumbers(10, 0))
print(sumNaturalNumbers_Alpha(10))