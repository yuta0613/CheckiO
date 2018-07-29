def find_message(text: str) -> str:
    import re 
    result = ""
    if text:
        for ch in text.split():
            result += ch 
    
        results = re.findall('[A-Z]', result)
        ans = ""
        for i in results:
            ans += i 
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
