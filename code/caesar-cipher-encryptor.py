def to_encrypt(text, delta):
    s = [ord(x) + delta for x in text]

    ans = []

    for x in s:
        if x > ord("z"):
            x = x - ord("z") + ord("a") - 1
        if x < ord("a"):
            x = x + (ord("z") - ord("a")) + 1
        if x == (32 + delta) + (ord("z") - ord("a")) + 1 or x == (32 + delta) - ord("z") + ord("a") - 1:
            x = 32
        ans.append(x)

    ans = "".join([chr(x) for x in ans])

    return ans

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")