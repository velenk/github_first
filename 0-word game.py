print("K")
cishu = 1
temp = input("cai cai kan:")
guess = int(temp)
if guess != 8:
    print("SB")
    cishu = cishu + 1
    if guess > 8:
        print('da')
    else:
        print('xiao')
    while guess != 8 and cishu < 5:
        temp = input("zai cai cai kan:")
        guess = int(temp)
        if guess != 8:
            print("SB")
            cishu = cishu + 1
            if guess > 8:
                print('da')
            else:
                print('xiao')
if cishu != 5:
    print("yes")
else:
    print('MDZZ')
print('bye')
