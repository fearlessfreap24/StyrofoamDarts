import xml.etree.ElementTree as ET
import random as r


# function to coutn items in sub trees of xml file
def count(thing):
    cnt = 0
    for item in thing:
        cnt += 1

    return cnt


# parse xml tree
tree = ET.parse('inventory.xml')
# set root of tree
root = tree.getroot()

# guns = root[0]
# magazines = root[1]
# bodyparts = root[2]

# get gun count
numguns = count(root[0])
# get magazine count
nummags = count(root[1])
# get body part count
numbodyparts = count(root[2])


class Shootem():

    def __init__(self):
        self.gun = root[0][r.randint[1, numguns-1]]
        self.mag = root[1][r.randint(1,nummags)-1]
        self.count = 0

    def getgun(self):
        name = self.gun[0]
        return name

    def getmag(self):
        magazine = self.mag[0]
        if self.gun[1] == "manual":
            return ""
        else:
            return magazine

    def getcount(self):







sh = Shootem()

print(sh.selectgun())
# # set random body part text
# bodypart = root[2][r.randint(1,numbodyparts)-1].text
# # get capacity of random magazine
# magazine = root[1][r.randint(1,nummags)-1][1].text
# # get random shot count
# shotcount = r.randint(1,int(magazine))
#
# # print shot statement
# print(f'you were shot with a {gun} in the {bodypart} {shotcount} times.')
