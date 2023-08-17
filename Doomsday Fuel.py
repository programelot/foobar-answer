'''
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

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
Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
Output:
    [7, 6, 8, 21]

Input:
Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    [0, 3, 2, 9, 14]

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]
'''

def frac(x, y):
    return (x,y)

def gcd(a,b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a < b:
        (a, b) = (b, a)
    while True:
        if a % b == 0:
            return b
        (a,b) = (b, a%b)

def lcm(a, b):
    g = gcd(a,b)
    return a * b //g

def normalize(c):
    if c[0] == 0:
        return (0, 1)
    dom = gcd(c[0], c[1])
    return (c[0]//dom, c[1]//dom)

def addFrac(a,b):
    c = (a[0] * b[1] + a[1] * b[0] , a[1] * b[1])
    return normalize(c)

def divFrac(a,b):
    c = (a[0] * b[1] , a[1] * b[0])
    return normalize(c)

def mulFrac(a,b):
    c = (a[0] * b[0] , a[1] * b[1])
    return normalize(c)

def sumFrac(lst):
    ret = (0, 1)
    for e in lst:
        ret = addFrac(ret, e)
    return ret

def isNotZero(c):
    return c != (0, 1)

def isZero(c):
    return c == (0, 1)

def solution(m):
    n = len(m)
    am = [[frac(e, 1) for e in l] for l in m] #argumented m
    isNonTerminal = [False] * n
    for i in range(n):
        #normalize outgoing edges
        am[i][i] = frac(0,1)#remove self loops
        s = sumFrac(am[i])
        if isNotZero(s):#non terminal
            isNonTerminal[i] = True
            for j in range(n):
                am[i][j] = divFrac(am[i][j], s)
    for i in range(1, n):
        #remove edges related with nonterminals except starting vertex
        if isNonTerminal[i]:#non terminal
            #compute the bipass
            add = [[frac(0,1) for x in range(n) ] for y in range(n) ] 
            for j in range(n):
                if isNotZero(am[j][i]):#j => i
                    for k in range(n):
                        if isNotZero(am[i][k]):#i => k
                            add[j][k] = addFrac(add[j][k], mulFrac(am[j][i] ,am[i][k]))
            #remove edges
            for j in range(n):
                am[j][i] = frac(0,1)
            for k in range(n):
                am[i][k] = frac(0,1)
            #add bipasses
            for j in range(n):
                for k in range(n):
                    am[j][k] = addFrac(am[j][k], add[j][k])
            #re-normalize
            for j in range(n):
                am[j][j] = frac(0,1)#remove self loops
                s = sumFrac(am[j])
                if isNotZero(s):#non terminal
                    for k in range(n):
                        am[j][k] = divFrac(am[j][k], s)
    lod = 1# lcm of denominator
    for i in range(n):
        lod = lcm(lod, am[0][i][1])
    ret = []
    for i in range(n):
        if not isNonTerminal[i]:
            ret.append(am[0][i][0] * lod // am[0][i][1])
    ret.append(lod)
    if ret == [0, 1]: #if there is no outgoing edges
        return [1, 1]
    return ret

'''
Excellent! You've destroyed Commander Lambda's doomsday device and saved Bunny Planet! But there's one small problem: the LAMBCHOP was a wool-y important part of the space station, and when you blew it up, you triggered a chain reaction that's tearing the station apart. Can you rescue the bunny workers and escape before the entire thing explodes?
Submission: SUCCESSFUL. Completed in: 44 mins, 9 secs.
'''
