# 452. Min Number of Arrows
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# Solution
We can sort the `points` by their second value in the tuple, then we set our `end` to the last element of the first tuple. Using this we can compare it to all the first values of the following tuples. If the value of end is less than the first value, that means the ballon isn't present in the interval and we must fire an additonal arrow.
