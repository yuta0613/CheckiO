def sun_angle(time):
    import datetime as dt

    d_1 = dt.datetime.strptime("6:00", "%H:%M")
    d_2 = dt.datetime.strptime("18:00", "%H:%M")

    # 入力文字列の時間型datetimeへの変換
    time = dt.datetime.strptime(time, "%H:%M")

    if time < d_1 or time > d_2:
        return "I don't see the sun!"
    #datetime.timedelta.secondsで引き算の結果を秒で取り出し、角度/secで演算する
    ans = ((time - d_1).seconds) * (180 / 43200)
    return ans


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")