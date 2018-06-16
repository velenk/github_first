jiati = int(input('甲体力:'))
yiti = int(input('乙体力:'))
jiasu = int(input('甲速度:'))
yisu = int(input('乙速度:'))
jiajiqi = jiasu
yijiqi = yisu
fangxiang = ['头部', '躯干', '下盘', '左侧', '右侧']
jiagong = [0, 0, 0, 0, 0]
yigong = [0, 0, 0, 0, 0]
jiafang = [1, 0, 1, 1, 1]
yifang = [1, 0, 1, 1, 1]
huihe = 1
#设定基本变量
while jiati > 0 and yiti >0:
    jiachenggong = yichenggong = False
    if jiajiqi >= yijiqi:
        #集气判断决定出手
        jiagongfang = input('甲是否攻击:')
        if bool(int(jiagongfang)):
            jiafang = [1, 1, 1, 1]
            jiadianwei = int(input('甲攻击点位:'))
            for i in range(5):
                if jiadianwei > 0:
                    jiagong[i] = int(input(fangxiang[i] + ':'))
                if jiagong[i] == 1:
                    jiadianwei -= 1
                #设定攻击
            if jiagong[0] * yifang[0] + jiagong[1] * yifang[1] + jiagong[2] * yifang[2] + jiagong[3] * yifang[3] + jiagong[4] * yifang[4] > 0:
                jiachenggong = True
            if jiachenggong == True:
                yiti -= 1
                print('乙受到伤害')
            else:
                yijiqi += yisu
        else:
            jiadianwei = int(input('甲防御点位:'))
            for i in range(5):
                if jiadianwei > 0 and jiafang[i] == 1:
                    jiafang[i] -= int(input(fangxiang[i] + ':'))
                    if jiafang[i] == 0:
                        jiadianwei -= 1
                #设定防御
        yijiqi += yisu
    else:
        yigongfang = input('乙是否攻击:')
        if bool(int(yigongfang)):
            yifang = [1, 1, 1, 1]
            yidianwei = int(input('乙攻击点位:'))
            for i in range(5):
                if yidianwei > 0:
                    yigong[i] = int(input(fangxiang[i] + ':'))
                if yigong[i] == 1:
                    yidianwei -= 1
            if yigong[0] * jiafang[0] + yigong[1] * jiafang[1] + yigong[2] * jiafang[2] + yigong[3] * jiafang[3] + yigong[4] * jiafang[4] > 0:
                yichenggong = True
            if yichenggong == True:
                jiati -= 1
                print('甲受到伤害')
            else:
                jiajiqi += jiasu
        else:
            yidianwei = int(input('乙防御点位:'))
            for i in range(5):
                if yidianwei > 0 and yifang[i] == 1:
                    yifang[i] -= int(input(fangxiang[i] + ':'))
                    if yifang[i] == 0:
                        yidianwei -= 1
        jiajiqi += jiasu
    if jiati <= 0:
        print('甲方败北')
        break
    if yiti <= 0:
        print('乙方败北')
        break
    jiagong = [0, 0, 0, 0, 0]
    yigong = [0, 0, 0, 0, 0]
    print('回合数' + str(huihe))
    huihe += 1
    print('甲体力' + str(jiati) + '集气' + str(jiajiqi))
    print('乙体力' + str(yiti) + '集气' + str(yijiqi))
    #数据显示
print('甲体力:' + str(jiati))
print('乙体力:' + str(yiti))
print('战斗' + str(huihe) + '回合')
#结果显示
