#!/usr/bin/env python
# coding: utf-8
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

def main():
    # print(getNumberOfRoutes(2, 2))
    # print(getNumberOfRoutes(3, 3))
    print(getNumberOfRoutes(20, 20))

# The algorithm uses divide and conquer scheme:
# From every vertex you can only travel to the right or down, and you have to
# go from the "x" to the "o".
#   x--+--+--+
#   |  |  |  |
#   +--+--+--+
#   |  |  |  |
#   +--+--+--+
#   |  |  |  |
#   +--+--+--o
# The first turn we can go right or down:
#   Right:          Down:           For each possible decision we have a
#   x→→+--+--+      x               smaller grid. So, we can solve it by
#      |  |  |      ↓               saying:
#      +--+--+      +--+--+--+
#      |  |  |      |  |  |  |      routes(w, h)=routes(w-1, h)+routes(w, h-1)
#      +--+--+      +--+--+--+      routes(1, h)=h+1
#      |  |  |      |  |  |  |      routes(w, 1)=w+1
#      +--+--+      +--+--+--+
def getNumberOfRoutes(width, height, buffer = dict()):
    if height == 1:
        return width + 1
    elif width == 1:
        return height + 1
    else:
        try:
            return buffer[(width, height)]
        except KeyError:
            routes  = getNumberOfRoutes(width - 1, height, buffer)
            routes += getNumberOfRoutes(width, height - 1, buffer)
            buffer[(width, height)] = routes
            buffer[(height, width)] = routes
            return routes

if __name__ == "__main__":
    main()
