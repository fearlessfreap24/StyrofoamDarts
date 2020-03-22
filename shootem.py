import xml.etree.ElementTree as ET
import random as r


# function to count items in sub trees of xml file
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


class Shootem:

    def __init__(self):
        self.gun = root[0][r.randint(1, numguns-1)]
        self.mag = root[1][r.randint(1, nummags-1)]
        self.body = root[2][r.randint(1, numbodyparts-1)]

    def getgun(self):
        name = self.gun[0].text
        return name

    def getmag(self):
        magazine = self.mag[0].text
        if self.gun[1].text == "manual":
            return ""
        else:
            return magazine

    def getcount(self):
        if self.gun[1].text == "manual":
            return self.gun[2].text
        else:
            return self.mag[1].text

    def getbodypart(self):
        return self.body.text

    def printshoot(self, author):
        gun = self.getgun()
        mag = self.getmag()
        cnt = self.getcount()
        body = self.getbodypart()

        if mag == "":
            return f'{author} was shot in the {body} {r.randint(1, int(cnt))} times with a {gun} .'
        else:
            return f'{author} was shot in the {body} {r.randint(1, int(cnt))} times with a {gun}' \
                   f' holding a {mag} magazine .'
