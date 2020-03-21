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

gun = root[0][r.randint(1,numguns)-1][0].text
bodypart = root[2][r.randint(1,numbodyparts)-1].text
magazine = root[1][r.randint(1,nummags)-1][1].text
shotcount = r.randint(1,int(magazine))
print(f'you were with a {gun} in the {bodypart} {shotcount} times.')
