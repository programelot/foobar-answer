'''
Braille Translation
===================

Because Commander Lambda is an equal-opportunity despot, they have several visually-impaired minions. But Lambda never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and -- since you'll be promoting efficiency at the same time -- increase your chances of a promotion. 

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "100100101010100110100010".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

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
solution.solution("code")
Output:
    100100101010100110100010

Input:
solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

-- Java cases --
Input:
Solution.solution("code")
Output:
    100100101010100110100010

Input:
Solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
Solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
    '''

def solution(plaintext):
    ret = ""
    A = ord('A')
    Z = ord('Z')
    a = ord('a')
    for e in plaintext:
        v = ord(e)
        if A <= v <= Z:
            ret += "000001"
            v = v - A + a
        e = chr(v)
        if e == ' ':
            ret += "000000"
        elif e == 'a':
            ret += "100000"
        elif e == 'b':
            ret += "110000"
        elif e == 'c':
            ret += "100100"
        elif e == 'd':
            ret += "100110"
        elif e == 'e':
            ret += "100010"
        elif e == 'f':
            ret += "110100"
        elif e == 'g':
            ret += "110110"
        elif e == 'h':
            ret += "110010"
        elif e == 'i':
            ret += "010100"
        elif e == 'j':
            ret += "010110"
        elif e == 'k':
            ret += "101000"
        elif e == 'l':
            ret += "111000"
        elif e == 'm':
            ret += "101100"
        elif e == 'n':
            ret += "101110"
        elif e == 'o':
            ret += "101010"
        elif e == 'p':
            ret += "111100"
        elif e == 'q':
            ret += "111110"
        elif e == 'r':
            ret += "111010"
        elif e == 's':
            ret += "011100"
        elif e == 't':
            ret += "011110"
        elif e == 'u':
            ret += "101001"
        elif e == 'v':
            ret += "111001"
        elif e == 'w':
            ret += "010111"
        elif e == 'x':
            ret += "101101"
        elif e == 'y':
            ret += "101111"
        elif e == 'z':
            ret += "101011"
    return ret
