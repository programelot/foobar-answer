'''
Bringing a Gun to a Trainer Fight
=================================

Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately, you grabbed a beam weapon from an abandoned storeroom while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the bunny trainers: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the bunny trainer, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, trainer_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the trainer's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite trainer, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite trainer are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite trainer were positioned in a room with dimensions [3, 2], your_position [1, 1], trainer_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite trainer (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite trainer with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite trainer with a total shot distance of sqrt(5).

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
Solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9

-- Python cases --
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9
'''

def sig(x):
    return 1 if x > 0 else -1

def gcd(x, y):
    if x < 0:
        x = -x
    if y < 0 :
        y = -y
    if x < y:
        (x,y) = (y,x)
    while True:
        if x%y == 0:
            return y
        (x,y) = (y, x%y)

def line(p1, p2):
    # 0 = ax + by + c
    #return (a,b,c)
    (a,b,c) = (p2[1] - p1[1], p1[0] - p2[0], p1[1]*p2[0] - p1[0]*p2[1])
    if a == 0 and b == 0:
        return (0, 0, sig(c))
    if a == 0 and c == 0:
        return (0, sig(b), 0)
    if b == 0 and c == 0:
        return (sig(a), 0, 0)
    if a == 0:
        g = gcd(b, c)
        return (a//g,b//g,c//g)
    if b == 0:
        g = gcd(a, c)
        return (a//g,b//g,c//g)
    if c == 0:
        g = gcd(a, b)
        return (a//g,b//g,c//g)
    g = gcd(gcd(a,b),c)
    return (a//g,b//g,c//g)

def dist(p1, p2):
    #return distance ** 2
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    
def solution(dimensions, your_position, trainer_position, distance):
    dx, dy = dimensions
    dp = distance ** 2#distance power
    minDim = min(dx, dy)
    batch = distance//minDim + 1
    yx, yy = your_position
    tx, ty = trainer_position
    lineDict = dict()
    for y in range(-batch, batch + 1):
        for x in range(-batch, batch + 1):
            ttx, tty = tx, ty
            if x%2 == 0:
                ttx = tx + x * dx
            else:
                ttx = (x + 1) * dx - tx
            if y%2 == 0:
                tty = ty + y * dy
            else:
                tty = (y + 1) * dy - ty
            d = dist((ttx, tty), (yx, yy))
            if d <= dp:
                l = line((ttx, tty), (yx, yy))
                p = (ttx - yx, tty - yy)
                if l in lineDict:
                    if lineDict[l][0] > d:
                        lineDict[l] = (d,p)
                else:
                    lineDict[l] = (d, p)
    for y in range(-batch, batch + 1):
        for x in range(-batch, batch + 1):
            tyx, tyy = yx, yy
            if x%2 == 0:
                tyx = yx + x * dx
            else:
                tyx = (x + 1) * dx - yx
            if y%2 == 0:
                tyy = yy + y * dy
            else:
                tyy = (y + 1) * dy - yy
            d = dist((tyx, tyy), (yx, yy))
            if d <= dp:
                l = line((tyx, tyy), (yx, yy))
                p = (tyx - yx, tyy - yy)
                if l in lineDict:
                    if lineDict[l][0] > d:
                        del lineDict[l]
    lineLst = list(lineDict)
    n = len(lineLst)
    return n

'''
Submission: SUCCESSFUL. Completed in: 2 hrs, 32 mins, 26 secs.
'''
