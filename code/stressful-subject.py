def is_stressful(subj):
    if subj.endswith("!!!") or subj.isupper():
        return True

    ans = []
    for x in range(len(subj)):
        if not subj[x] == subj[x-1]:
            ans.append(subj[x])

    z  = "".join([ x.lower() for x in ans if x.isalpha()])

    if "help" in z or "asap" in z or "urgent" in z :
        return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
