'''
Distract the Trainers
=====================

The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. And thumb wrestling.

The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to supervising the bunny workers, and you don't want THAT to happen!

For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to training bunnies.

How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!

Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.

The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0

-- Java cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
Solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0
 '''


def isCyclic(x, y):
    cnt = 0
    while True:
        if x == y:
            return False
        if (x + y) % 2 == 1:
            return True
        if x > y:
            (x,y) = ((x - y)//2, y)
        else:
            (x,y) = (x, (y - x)//2)

def countMatch(G):
    n = len(G)
    M = [-1 for x in range(n)]
    for i in range(n):
        p = None if M[i] != -1 else findPath(G, M, i)        
        if p != None: #Path exists
            lp = len(p)//2
            for j in range(lp):#set Matching
                s = p[2 * j]
                v = p[2 * j + 1]
                M[s] = v
                M[v] = s
    return n - M.count(-1)

def findPath(G, M, src):
    #Graph G
    #Matching M
    
    n = len(G)
    #bfs from i
    q = [src]
    reachBy = [[]] * n
    reachBy[src] = [src]
    while q != []:
        nq = []
        for i in range(len(q)):
            x  = q[i]#current vertex
            p  = reachBy[x]
            for j in range(n):
                if G[x][j]:#e -> j
                    if M[j] == -1:
                        if j != src:
                            return p + [j]
                    else:
                        if reachBy[j] == []:
                            nq.append(M[j])
                            reachBy[j] = p + [j]
                            reachBy[M[j]] = p + [j, M[j]]
                        else:
                            cp = reachBy[j]
                            if len(cp) % 2 == 1:#cycle detected
                                for k in range(len(cp) - 1, - 1, -2):
                                    if cp[k] in p:#cycle closed
                                        break
                                    y, yn = cp[k], cp[k - 1] # new goThrough
                                    ##  x -> j -> M[j] -> y -> yn -> yp
                                    for yp in range(n):
                                        if G[yn][yp]:
                                            if M[yp] == -1:
                                                if yp != src:
                                                    return p + [j, M[j], y, yn, yp]
                                            elif reachBy[yp] == []:
                                                reachBy[j] = p + [j]
                                                reachBy[M[j]] = p + [j, M[j]]
                                                nq.append(M[yp])
                                                reachBy[yp]    = p + [j, M[j], y, yn, yp]
                                                reachBy[M[yp]] = p + [j, M[j], y, yn, yp, M[yp]]                                                
        q = nq
    return None
                
def solution(banana_list):
    n = len(banana_list)
    cyclic = [[False for x in range(n)] for y in range(n)]
    for y in range(n):
        for x in range(y + 1, n):
            isCycle = isCyclic(banana_list[x], banana_list[y])
            cyclic[y][x] = isCycle
            cyclic[x][y] = isCycle
    return n - countMatch(cyclic)
