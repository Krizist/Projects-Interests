import matplotlib.pyplot as plt
import numpy as np
import pandas
from mpl_toolkits.mplot3d import Axes3D
import random as rrand
from pylab import *
from numpy import *

def findCircle(p1, p2, center):
    x1, y1 = p1
    x2, y2 = p2
    cx, cy = center

    # ab = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    ac = ((x1-cx)**2 + (y1-cy)**2)**(0.5)

    return ac

def findR(p, center):
    x, y = p
    cx, cy = center
    return ((x-cx)**2 + (y-cy)**2)**0.5

startk = 0
endk = 0

x=np.arange(-50,50,1)
y=[e*e for e in x]
c=np.arange(-50,50,1)

    # i += rand.randrange(10, 50)
k = [i*i + rrand.random()*200 for i in c]
    # if(i == c[0]):
    #     startk = k
    # if(i == c[len(c)-1]):
    #     endk = k
plt.figure(1)
plt.plot(c, k, 'ro')
print (c[0])
print c[len(c)-1]
ax, ay = (c[0], k[0])
bx, by =  (c[len(c)-1], k[len(c)-1])
print ax, ay, bx, by
ab = ((ax-bx)**2 + (ay-by)**2)**(0.5)
slope = (k[0]-k[len(c)-1])/(c[0]-c[len(c)-1])
x = c[1] - c[0]
print 'ab'
print ab
farthest = (ab/2)/tan(pi/180)
print(farthest)
midx, midy = ((ax+bx)/2, (ay+by)/2)
step = 0
LSlist1 = []
LSlist = []
rlist1 = []
rlist = []
centerx1 = []
centery1 = []
while abs(step) < farthest:
    center = (midx + step, (-1/slope)*(step) + midy)
    centerx1.append(center[0])
    centery1.append(center[1])
    step += 5
    r = findCircle((ax, ay), (bx, by), center)
    print r
    cir = Circle((center[0], center[1]), radius=r,  fc='y', fill=False)
    gca().add_patch(cir)
    leastSqr = 0
    for i in range(1, len(c)-2):
        leastSqr += abs((c[i]-center[0])**2 + (k[i]-center[1])**2 - r**2)
    LSlist1.append(leastSqr)
    rlist1.append(r)

step = 0
centerx = []
centery = []
while abs(step) < farthest:
    center = (midx + step, (-1/slope)*(step) + midy)
    centerx.append(center[0])
    centery.append(center[1])
    step += -5
    r = findR((ax, ay), center)
    print r
    cir = Circle((center[0], center[1]), r,  fc='y', fill=False)
    # print cir
    # print r
    gca().add_patch(cir)
    leastSqr = 0.01
    for i in range(1, len(c)-2):
        leastSqr += abs((c[i]-center[0])**2 + (k[i]-center[1])**2 - r**2)
    LSlist.append(leastSqr)
    # print r
    rlist.append(r)

# plt.figure(1)
# print(centerx)
# print(centery)
# plt.plot(np.array(centerx), np.array(centery), 'ro')
plt.figure(2)
# plt.plot(np.array(rlist1), np.array(LSlist1))
# plt.plot(np.array(rlist), np.array(LSlist))
minLS1 = min(LSlist1)
minLS = min(LSlist)
if minLS < minLS1:
    minIndex = LSlist.index(minLS)
    bestR = rlist[minIndex]
    fitX, fitY = centerx[minIndex], centery[minIndex]
    print 'least square: ' + str(minLS) + ", radius: " + str(bestR)
    print 'center: (' + str(fitX) + ", " + str(fitY)+ ')'
else:
    minIndex = LSlist1.index(minLS1)
    bestR = rlist1[minIndex]
    fitX, fitY = centerx1[minIndex], centery1[minIndex]
    print 'least square: ' + str(minLS1) + ", radius: " + str(bestR)
    print 'center: (' + str(fitX) + ", " + str(fitY) + ')'

print 'hu'
# print r
# print np.array(r)
print 'hei'

plt.plot(np.array(rlist1), np.array(LSlist1))
plt.plot(np.array(rlist), np.array(LSlist))


plt.show()

