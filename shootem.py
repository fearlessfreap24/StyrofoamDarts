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

    # standard init - defining the items that wil lbe used to shoot
    def __init__(self):
        self.gun = root[0][r.randint(1, numguns-1)]
        self.mag = root[1][r.randint(1, nummags-1)]
        self.body = root[2][r.randint(1, numbodyparts-1)]

    def getgun(self):
        # get the name of the weapon chosen
        return self.gun[0].text

    def getmag(self):
        # return name of magazine
        return self.mag[0].text

    def getcount(self):
        # check if weapon is manual feed
        if self.gun[1].text == "manual":
            # return maxCap of weapon if manual feed
            return self.gun[2].text
        else:
            # return magazine cap
            return self.mag[1].text

    def getbodypart(self):
        # return name of body part
        return self.body.text

    def printshoot(self, author):
        # create variables for shoot statement
        gun = self.getgun()
        mag = self.getmag()
        cnt = self.getcount()
        body = self.getbodypart()

        # shoot statement for manual feed weapons
        if self.gun[1].text == "manual":
            return f'@{author} was shot in the {body} {r.randint(1, int(cnt))} times with a {gun} .'
        # shoot statement for magazine feed weapons
        else:
            return f'@{author} was shot in the {body} {r.randint(1, int(cnt))} times with a {gun}' \
                   f' holding a {mag} magazine .'
