def productOfFour(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    return productOfFour(n // 4)

print(productOfFour(16))