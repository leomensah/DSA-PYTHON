def productOfThree(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return productOfThree(n // 3)

print(productOfThree(27))