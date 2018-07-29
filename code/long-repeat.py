def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    # 連続文字数のリストを作成 ex [0, 2, 7, 8]
    line=line + " "
    count = []
    for i in range(len(line)):
        if  line[i] != line[i - 1] or line[i] == " ":
            count.append(i)
    # リストをもとに最大連続文字数を求める
    ans = []
    for i in range(len(count)):
        x = count[i] - count[i - 1]
        ans.append(x)

    return max(ans)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')