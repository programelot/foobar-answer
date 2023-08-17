'''
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

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
solution.solution(0, 1)
Output:
    3

Input:
solution.solution(19, 36)
Output:
    1

-- Java cases --
Input:
Solution.solution(19, 36)
Output:
    1

Input:
Solution.solution(0, 1)
Output:
    3
'''

def solution(src, dst):
    inf = float("inf")
    dist = [[inf for x in range(8)] for y in range(8)]
    src = (src%8, src//8)
    dst = (dst%8, dst//8)
    dist[src[0]][src[1]] = 0
    q = [(src[0],src[1])]
    currentDist = 0
    while dist[dst[0]][dst[1]] == inf:
        currentDist += 1
        nq = []
        for e in q:
            ex = e[0]
            ey = e[1]
            for t in [(ex-2, ey-1), (ex-1, ey-2), (ex-2, ey+1), (ex-1, ey+2), (ex+2, ey-1), (ex+1, ey-2), (ex+2, ey+1), (ex+1, ey+2)]:
                if (0 <= t[0] < 8) and (0 <= t[1] < 8):
                    if dist[t[0]][t[1]] == inf:
                        dist[t[0]][t[1]] = currentDist
                        nq.append((t[0],t[1]))
        q = nq     
    return dist[dst[0]][dst[1]]

'''
Submission: SUCCESSFUL. Completed in: 17 mins, 45 secs.
'''
