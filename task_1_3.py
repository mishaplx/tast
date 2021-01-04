# привести секунды к виду h:mm:ss
sec = int(input())
if sec > 86400:
    sec1 = sec % 86400
    h = sec1 // 3600
    mm = (sec1 % 3600) // 60
    ss = (sec1 % 3600) % 60
    if mm < 10 and ss < 10:
        print("{}:0{}:0{}".format(h, mm, ss))
    elif mm < 10 and ss > 10:
        print("{}:0{}:{}".format(h, mm, ss))
    elif mm > 10 and ss < 10:
        print("{}:{}:0{}".format(h, mm, ss))
    else:
        print("{}:{}:{}".format(h, mm, ss))
else:
    h = sec // 3600
    mm = (sec % 3600) // 60
    ss = (sec % 3600) % 60
    if mm < 10 and ss < 10:
        print("{}:0{}:0{}".format(h, mm, ss))
    elif mm < 10 and ss > 10:
        print("{}:0{}:{}".format(h, mm, ss))
    elif mm > 10 and ss < 10:
        print("{}:{}:0{}".format(h, mm, ss))
    else:
        print("{}:{}:{}".format(h, mm, ss))
