import random
secret = random.randint(1, 999)
cishu = 1
limit = 12
temp = input("cai cai kan:")
guess = int(temp)
if guess != secret:
    print("SB")
    cishu = cishu + 1
    if guess > secret:
        print('da')
    else:
        print('xiao')
    while guess != secret:
        temp = input("zai cai cai kan:")
        guess = int(temp)
        if guess != secret:
            print("SB")
            cishu = cishu + 1
            if guess > secret:
                print('da')
            else:
                print('xiao')
        if cishu == limit:
            break
if cishu != limit:
    print("yes")
else:
    print('MDZZ')
print('bye')
