import random
import math
text = open('math3.txt', 'wb')
ans = open('answer3.txt', 'wb')

def mathe(digits, rang, num):
    first = random.randint(11, rang)
    text.write(str(first))
    for i in range(0, num-1):
        op = random.randint(0, 1)
        boo = True
        if first > (rang - math.pow(10, digits-1)):
            op = 0
        elif first < 10:
            op = 1
        if op:#+
            j = 100
            while j + first > 100:
                j = randomNum(boo, first, digits, rang)
            text.write(" + ")
            text.write(str(j))
            first = first + j
        else:
            #-
            boo = False
            j = 10000000000000
            while j > first:
                j = randomNum(boo, first, digits, rang)
            text.write(" - ")
            text.write(str(j))
            first = first - j
    text.write(" = ")
    text.write("\n")
    ans.write("\n")
    return first


def randomNum(boo, summ, digits, rang):
    times10 = math.pow(10, digits-1)
    lsd = int(summ%(times10))
    msd = int(summ/times10)
    #print lsd
    if boo:
        #+
        ##print 10-msd
        if lsd <= 1:
            lsd+=2
        jinw = int(random.randint(10-lsd, 9))
        w = int(random.randint(0, 10-msd-2))
        ret = int(w*times10+jinw)
        return int(ret)
    else:
        #-
        #print 10-lsd
        if lsd == 9:
            lsd-=1
        jiew = int(random.randint(lsd, 9))
        if msd < 2:
            w = 0
        else:
            w = int(random.randint(0, msd-1))
        ret = w*times10+jiew
        return int(ret)

# def countDigits(num):
#     count = 0
#     while (num > 10):
#         num /= 10
#         count+=1
#     return count

def main(nums):
    for i in range(0, nums-1):
        text.write(str(i+1))
        text.write(") ")
        answ = mathe(2, 99, 2)
        ans.write(str(i+1))
        ans.write(". ")
        ans.write(str(answ))
    text.close()

main(101)
