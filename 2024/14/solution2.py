import sys
import re

width,height = 101,103

class Robot:
    pattern = re.compile("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

    @staticmethod
    def from_pattern(line):
        match = Robot.pattern.fullmatch(line)

        return Robot(
            (int(match.group(1)),int(match.group(2))),
            (int(match.group(3)),int(match.group(4)))
        )

    def __init__(self,p,v):
        self.p = p
        self.v = v

    def step(self, n = 1):
        self.p = (self.p[0] + n * self.v[0], self.p[1] + n * self.v[1])
        self.p = (self.p[0] % width, self.p[1] % height)
        if (self.p[0] < 0):
            self.p = (self.p[0] + width, self.p[1])
        if (self.p[1] < 0):
            self.p = (self.p[0], self.p[1] + height)


    def quadrant(self):
        if self.p[0] == width // 2 or self.p[1] == height // 2:
            return None
        
        q = 0
        if self.p[0] > width // 2:
            q += 1
        if self.p[1] > height // 2:
            q += 2
        return q

robots = []
for line in map(str.rstrip, sys.stdin):
    robot = Robot.from_pattern(line)
    robots.append(robot)

def printrobots():
    s = set([robot.p for robot in robots])
    for i in range(width):
        for j in range(height):
            if ((i,j) in s):
                print ('0', end="")
            else:
                print ('.', end="")
        print()
    print(' ======== ')
            


for seconds in range(10000000):
    d = {None: 0,0: 0, 1: 0, 2: 0, 3: 0}
    for robot in robots:
        robot.step()
        d[robot.quadrant()] += 1
    if (max(list(d.values())) > 250):
        print(seconds)
        printrobots()
