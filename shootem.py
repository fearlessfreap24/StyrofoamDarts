import xml.etree.ElementTree as ET
import random as r


def count(thing):
    cnt = 0
    for item in thing:
        cnt += 1

    return cnt


tree = ET.parse('inventory.xml')
root = tree.getroot()

# guns = root[0]
# magazines = root[1]
# bodyparts = root[2]

numguns = count(root[0])
nummags = count(root[1])
numbodyparts = count(root[2])

print(f'you got shot with a {root[0][r.randint(1,4)-1].tag()}')