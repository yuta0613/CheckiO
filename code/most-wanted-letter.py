def checkio(text: str) -> str:
    import re
    string = re.sub('((?![A-Za-z]).)*', "", text ).lower()
    counter = {}

    for c in string:
        if not c in counter:
            counter[c] = 1
        else:
            counter[c] += 1


    counter = list(counter.items())        

    counter = sorted(counter, key=lambda x: x[0])
    ans = sorted(counter, key=lambda x: x[1], reverse=True)[0][0]
    return ans
    
if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
