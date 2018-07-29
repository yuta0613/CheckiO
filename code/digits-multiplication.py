def checkio(number: int) -> int:
    num = list(map(int, str(number)))
    ans = 1
    for i in range(len(num)):
        if num[i] == 0:
            pass
        else:
            ans *= num[i]
    return ans
   
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
