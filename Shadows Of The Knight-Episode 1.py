import sys
import math
w, h = [int(i) for i in input().split()] #w- width of building, h-height of building
n = int(input())  # maximum number of turns before game over. This info is quite irrelavent to my code but wtv 
x, y = [int(i) for i in input().split()] #x and y are batman's initial coordinates

# Binary search concept. First step is to setup search area
minx=miny = 0
maxx = w
maxy = h

# game loop
while True:
    # the direction of the bombs from batman's current location: U, UR, R, DR, D, DL, L or UL
    # Manipulate the search area using if and elif statements 
    direction = input() 
    if 'U' in direction:
        maxy = y - 1
    elif 'D' in direction:
        miny = y + 1
    if 'L' in direction:
        maxx = x - 1
    elif 'R' in direction:
        minx = x + 1
    x = (minx+maxx) // 2 #use floor division "//" instead of division "/" operator to obtain int instead of float 
    y = (miny+maxy) // 2
    print(x,y)
