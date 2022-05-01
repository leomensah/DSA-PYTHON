def powerOfTwo(num: int) -> bool:
    if num == 0:
        return False
    if num == 1:
        return True
    if num % 2 != 0:
        return False
    return powerOfTwo(num // 2)

print(powerOfTwo(16))