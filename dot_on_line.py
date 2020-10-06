from dot import Dot
import math
import tests

# calculate distance
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


# this function returns 1 if dotc is on the segment dota-dotb. else returns 0
def is_dot_on_line(dota, dotb, dotc):
    if dota.equal(dotc):  # if dotc is equal to one of the other dots
        return 1
    if dotb.equal(dotc):
        return 1
    if dota.x1 == dotb.x1 == dotc.x1:           # if the "x" of all the dots is the same
        if dota.x2 > dotb.x2:
            if dotb.x2 < dotc.x2 < dota.x2:
                return 1
            else:
                return 0
        else:
            if dota.x2 < dotc.x2 < dotb.x2:
                return 1
            else:
                return 0
    if dota.x2 == dotb.x2 == dotc.x2:               # if the "y" of all the dots is the same
        if dota.x1 > dotb.x1:
            if dotb.x1 < dotc.x1 < dota.x1:
                return 1
            else:
                return 0
        else:
            if dota.x1 < dotc.x1 < dotb.x1:
                return 1
            else:
                return 0
    else:
        dist_ab = distance(dota.x1, dota.x2, dotb.x1, dotb.x2)
        dist_bc = distance(dotb.x1, dotb.x2, dotc.x1, dotc.x2)
        dist_ac = distance(dota.x1, dota.x2, dotc.x1, dotc.x2)
        if dist_ab == dist_bc + dist_ac:
            return 1
        else:
            return 0
