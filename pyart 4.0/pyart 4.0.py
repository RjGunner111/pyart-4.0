import time
import turtle

import keyboard
import webcolors
import socket
import threading
from tabulate import tabulate
import os
import csv

# modules to install: keyboard, webcolors, tabulate, you can automatically run this in a cmd file named "modulesinstall.cmd"
# don't trust it? open it in notepad and see for yourself that it installs the modules necessary to run this file.

# default loop variable
loopss = 0

# keeps the graphical interface going
turtlw = 1

scary = os.path.dirname(__file__)

# the file containing all colors
csvi = f"{scary}/colors.csv"

# prevents an exception for existing color for wrong reasons
exceptionprevent = []

# prevents character exception
exceptionchar = []

# removes duplicates
dupre = []

# stores the name color
dupe = []

# removes loop duplicates
loodup = []

# default length character
sp = 20

# removes previous lists of loop colors
ipx = 0

# initial color
p = 0

# keeps track of amount of colors entered
ipn = 0

# color definition
colorr = []

# selected name for definition
sepe = []

# selected color loop def
loose = []

# saves the 3 binary hexes
hpz = []

# enumerate for list of colors
colorenum = []

# keeps track of names input of loop
nameenum = []

# saves the 6 binary hexes
hdr = []

# keeps track so it can know what to append to loopcolorw
colors = []

# 0 = dark theme, 1 = light theme
light = 0

# arguments to bypass the "main loop not in main thread" exception
reset = 0
lost = 0
lin = 0
tehlel = ""
loser = 0
funcol = ""
strinf = ""
tryagain = ""
idiot = ""
piss = ""
err = 0
loopenum = 0
wtsh = ""
wtfcolor = ""

# reset function
def begin():
    global lost
    lost -= 1
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, -22)
    turtle.speed("slowest")
    turtle.pendown()


def coloren(no):
    global io, ipn, ipns
    try:
        io = int(no)
    except ValueError:
        io = 0
        print("Invalid base number of loops, please try again")
    try:
        ipns = ipns
    except NameError:
        ipns = 1
    if io != 0:
        ipn += 1
        if ipns != 0:
            if ipns == 1:
                ipns = io
            else:
                ipns -= 1
    return ipn


def colorgrab(troll):
    global piss, idiot
    if loopss == 0:
        for wtf in turtl.colorw:
            if wtf == turtl.colorw[p]:
                dum = wtf.strip("#")
                mud = tryagain.strip("#")
                try:
                    idiot = webcolors.hex_to_name(tryagain)
                except ValueError:
                    try:
                        idiot = webcolors.hex_to_name(turtl.colorw[p])
                    except ValueError:
                        pass
                if idiot == wtf:
                    ryd = tuple(int(mud[i:i + 2], 16) for i in (0, 2, 4))
                elif len(dum) < 5:
                    ryn = str(hdr[0]).strip("#")
                    ryd = tuple(int(ryn[i:i + 2], 16) for i in (0, 2, 4))
                else:
                    ryd = tuple(int(dum[i:i + 2], 16) for i in (0, 2, 4))
                piss = str(ryd[troll])
                return piss
    elif loopss == 1:
        for wtf in colorenum:
            if wtf == colorenum[loopenum]:
                dum = wtf.strip("#")
                mud = tryagain.strip("#")
                try:
                    idiot = webcolors.hex_to_name(tryagain)
                except ValueError:
                    try:
                        idiot = webcolors.hex_to_name(colorenum[loopenum])
                    except ValueError:
                        pass
                if idiot == wtf:
                    ryd = tuple(int(mud[i:i + 2], 16) for i in (0, 2, 4))
                elif len(dum) < 5:
                    ryn = str(hdr[0]).strip("#")
                    ryd = tuple(int(ryn[i:i + 2], 16) for i in (0, 2, 4))
                else:
                    ryd = tuple(int(dum[i:i + 2], 16) for i in (0, 2, 4))
                piss = str(ryd[troll])
                return piss


def colornaming(newgames, origin, wtsh):
    global hell, loopcolor
    if wtsh != "":
        try:
            if loopss == 1:
                if origin != "":
                    for lold in nameenum:
                        if origin == lold:
                            hell = lold
            for names in colorr:
                if names[2] == newgames:
                    if names[3] == wtsh[0] and names[4] == wtsh[1] and names[5] == wtsh[2]:
                        newgames = names[1]
                        origin = newgames
                elif origin != "":
                    if names[1].lower() == hell:
                        newgames = names[1]
                        origin = newgames
            if newgames != origin:
                raise NameError
            else:
                return newgames
        except NameError:
            try:
                newgames = webcolors.hex_to_name(newgames)
                return newgames
            except ValueError:
                closecolor = wtsh
                newgames = turtl.closest_hex_colour(closecolor)
                return newgames
    else:
        try:
            for names in colorr:
                if names[2] == newgames:
                    if names[1].lower() == origin.lower():
                        newgames = names[1]
            if newgames.lower() != origin.lower():
                raise NameError
            else:
                return newgames
        except NameError:
            try:
                if turtl.colorw[p] != hdr[0]:
                    raise ValueError
                else:
                    newgames = webcolors.hex_to_name(newgames)
                    return newgames
            except ValueError:
                closecolor = webcolors.hex_to_rgb(turtl.colorw[p])
                newgames = turtl.closest_hex_colour(closecolor)
                return newgames


# how the conversion from just python to python and c# was possible
def network():
    global sp, reset, lost, lin, tehlel, loser, funcol, strinf, tryagain, idiot, piss, newnames, bas, \
        loopss, err, p, ipns, colorpp, enume, newlist, loopenum, newname, wtfcolor, newcol, wtshit, WTF \
    , loopcolor
    server = socket.socket()
    server.bind(("localhost", 1234))
    while turtlw != 0:
        server.listen()
        (client, ipsec) = server.accept()
        data = client.recv(1024)
        lss = str(data)
        try:
            if lss == "b'goup'":
                if loopss == 0:
                    turtl.colorcontrolup()
                elif loopss == 1:
                    if loopenum < len(colorenum) - 1:
                        loopenum += 1
                    else:
                        loopenum = 0
            elif lss == "b'godown'":
                if loopss == 0:
                    turtl.colorcontroldown()
                elif loopss == 1:
                    if loopenum > 0:
                        loopenum -= 1
                    else:
                        loopenum = len(colorenum) - 1
            elif lss == "b'recon'":
                bit = str(sp).encode()
                client.send(bit)
            elif lss == "b'spedup'":
                turtl.spine()
                bit = str(sp).encode()
                client.send(bit)
            elif lss == "b'speddown'":
                turtl.spike()
                bit = str(sp).encode()
                client.send(bit)
            elif lss == "b'reverse'":
                reset += 1
            elif lss == "b'lost'":
                lost += 1
            elif lss == "b'light'":
                lin += 1
            elif lss == "b'colordef'":
                if loopss == 0:
                    turtl.colordef()
                elif loopss == 1:
                    turtl.loopdef()
                bit = str(tehlel).encode()
                client.send(bit)
            elif lss == "b'enumerate'":
                if loopss == 0:
                    enume = len(turtl.colorw)
                elif loopss == 1:
                    enume = len(colorenum)
                bit = str(enume).encode()
                client.send(bit)
            elif lss.replace("'", "").endswith("getlist"):
                newnum = int(lss.lstrip("b").replace("'", "").replace(" getlist", ""))
                if loopss == 0:
                    newlist = turtl.colorw[newnum]
                    newno = webcolors.hex_to_rgb(newlist)
                    try:
                        newcol = colornaming(newlist, wtshit, "")
                    except NameError:
                        try:
                            newcol = colornaming(newlist, wtfcolor, "")
                        except IndexError:
                            newcol = " "
                    try:
                        if wtshit == newcol.lower() and newnum == 6 or \
                                wtshit.startswith("#") and newnum == 6:
                            if not wtshit.startswith("#"):
                                newname = wtshit
                                newname = str(newname + " (Custom)")
                            else:
                                newname = colornaming(wtshit, "", newno)
                                newname = str(newname + " (Custom)")
                        else:
                            newname = colornaming(newlist, "", newno)
                    except NameError:
                        newname = colornaming(newlist, "", newno)
                elif loopss == 1:
                    newlist = colorenum[newnum]
                    newns = nameenum[newnum]
                    newp = newlist.strip("#")
                    newno = tuple(int(newp[i:i + 2], 16) for i in (0, 2, 4))
                    if newns != " ":
                        newname = colornaming(newlist, newns, newno)
                    else:
                        newname = colornaming(newlist, "", newno)
                bit = newname.title().encode()
                client.send(bit)
            elif lss.replace("'", "").endswith("custom"):
                wtfcolor = lss.lstrip("b").replace("'", "").replace(" custom", "")
                turtl.ap(wtfcolor)
                time.sleep(0.1)
                if loser == 1:
                    loser -= 1
                    try:
                        if wtshit != dupe[0]:
                            turtl.ap(wtshit)
                    except (IndexError, NameError):
                        pass
                    bit = b"WTF"
                    client.send(bit)
                    loser = 1
                else:
                    time.sleep(0.1)
                    wtshit = wtfcolor
                    if not wtfcolor.startswith("#"):
                        newnames = dupe[0]
                    else:
                        asp = webcolors.hex_to_rgb(wtfcolor)
                        newnames = colornaming(wtfcolor, "", asp)
                    bit = str(str(len(turtl.colorw)) + f" {newnames.title()} (Custom) OK").encode()
                    client.send(bit)
                if turtl.colorw[p] != turtl.colorw[len(turtl.colorw) - 1] and loser != 1:
                    p = len(turtl.colorw) - 1
                elif loser == 1:
                    loser -= 1
                    p = 0
            elif lss.replace("'", "").endswith("change"):
                precolor = lss.lstrip("b").replace("'", "").replace(" change", "")
                if loopss == 0:
                    turtl.colorno2(precolor)
                elif loopss == 1:
                    loopenum = int(precolor)
            elif lss.replace("'", "").endswith("loopappend"):
                loopcolor = lss.lstrip("b").replace("'", "").replace(" loopappend", "")
                if not loopcolor.startswith("#"):
                    nameenum.append(loopcolor)
                else:
                    nameenum.append(" ")
                coloren(bas)
                turtl.colorloop(loopcolor, bas)
                if ipn == 0 and err != 1:
                    colorpp = p
                    for i in turtl.loopcolorw:
                        colorenum.append(i)
                    bit = b"DONE"
                    client.send(bit)
                elif err == 1:
                    err -= 1
                    bit = b"WTF"
                    client.send(bit)
                else:
                    bit = b"OK"
                    client.send(bit)
            elif lss.replace("'", "").endswith("loopbase"):
                loopbass = lss.lstrip("b").replace("'", "").replace(" loopbase", "")
                try:
                    bas = int(loopbass)
                    bit = b"OK"
                    client.send(bit)
                except ValueError:
                    bit = b"WTF"
                    client.send(bit)
            elif lss == "b'endloop'":
                loopss -= 1
                time.sleep(0.1)
                colorenum.clear()
                if turtl.colorw[p] != turtl.colorw[colorpp]:
                    p = colorpp
                bit = b"OK"
                client.send(bit)
            elif lss == "b'red'":
                colorgrab(0)
                bit = piss.encode()
                client.send(bit)
            elif lss == "b'green'":
                colorgrab(1)
                bit = piss.encode()
                client.send(bit)
            elif lss == "b'blue'":
                colorgrab(2)
                bit = piss.encode()
                client.send(bit)
            elif lss == "b'quit'":
                quitsd()
            else:
                bit = b"IGNORE"
                client.send(bit)
        except ValueError as e:
            WTF = f"An exception was made as ValueError: {str(e)} ENDERROR"
            bit = str(WTF).encode()
            client.send(bit)
        except IndexError as e:
            WTF = f"An exception was made as IndexError: {str(e)} ENDERROR"
            bit = str(WTF).encode()
            client.send(bit)


# prints the color definitions
def colord():
    print("0 = Red\n1 = Yellow\n2 = Green\n3 = Cyan\n4 = Blue\n5 = Magenta\n\n" 
          "NOTICE: Custom colors defined will be erased upon doing this command")


# quits the program
def quitsd():
    global turtlw
    turtlw -= 1


# the pyart app
class Turtle():
    def __init__(self):
        super().__init__()
        with open(csvi, "r", newline="") as csi:
            readi = csv.reader(csi)
            for row in readi:
                colorr.append(row)

    FONT = ("Arial", 14, "bold")

    colorw = [
        "#FF0000",
        "#FFFF00",
        "#00FF00",
        "#00FFFF",
        "#0000FF",
        "#FF00FF"
    ]

    loopcolorw = []

    loopcolorindex = []

    loopcolorwran = []

    loopcolorwinfo = []

    loopcolorwheader = ["Hexes", "RGB Values", "Color Names"]

    def __len__(self):
        return len(self.colorw)

    # increases the length of movement (50 is max)
    def spine(self):
        global sp
        if sp == 50:
            pass
        else:
            sp += 5

    # decreases the length of movement (10 is min)
    def spike(self):
        global sp
        if sp == 10:
            pass
        else:
            sp -= 5

    # light mode
    def lightmode(self):
        global light, lin
        lin -= 1
        if light == 0:
            light += 1
        elif light == 1:
            light -= 1
        pin = turtle.pos()
        self.sup()
        turtle.goto(pin)

    # predefined colors setup
    def colorno2(self, colornewp):
        global p, pi, loopss
        if loopss == 1:
            loopss = 0
        try:
            pi = int(colornewp)
        except ValueError:
            print("Invalid color definition, please try again")
        else:
            if pi > len(self.colorw) - 1:
                p = 0
                print("Invalid color definition, please try again")
            elif pi < 0:
                p = 0
                print("Invalid color definition, please try again")
            else:
                p = pi
        try:
            return pi
        except NameError:
            pass

    # custom hex color setup
    def ap(self, colornew):
        global p, pl, pf, pi, ui, loopss, loser, tryagain
        pi = colornew
        if loopss == 1:
            loopss -= 1
            colorenum.clear()
        if "#" in pi:
            pi = colornew
            for hexp in colorr:
                if hexp[2] == pi:
                    exceptionprevent.append(hexp)
                    pi = exceptionprevent[0][2]
                    vi = exceptionprevent[0][1]
                    if len(self.colorw) - 1 > 5:
                        self.colorw.pop()
                    self.colorw.append(pi)
                    if len(dupe) > 0:
                        dupe.pop()
                    dupe.append(vi)
                    if len(hdr) > 0:
                        hdr.clear()
                    hdr.append(pi)
        else:
            pi = colornew.title()
            for name1 in colorr:
                if name1[1] == pi:
                    exceptionprevent.append(name1)
                    pi = exceptionprevent[0][2]
                    vi = exceptionprevent[0][1]
                    if len(self.colorw) - 1 > 5:
                        self.colorw.pop()
                    self.colorw.append(pi)
                    if len(dupe) > 0:
                        dupe.clear()
                    if len(hpz) > 0:
                        hpz.clear()
                    if len(hdr) > 0:
                        hdr.clear()
                    dupe.append(vi)
            oi = str(pi).strip("#")
            ui = str()
            ore = len(oi)
            for char in oi:
                if ore > 4:
                    dupre.append(char)
                elif ore < 4:
                    ui += char + char
            if len(dupre) > 4:
                p3 = ("#" + dupre[0] + dupre[2] + dupre[4])

                if len(hpz) > 0:
                    hpz.clear()
                hpz.append(p3)
            else:
                p3 = ("#" + ui)
                if len(hdr) > 0:
                    hdr.clear()
                hdr.append(p3)
        if not exceptionprevent:
            pi = colornew
            li = pi.lower().strip("#")
            for char in li:
                dupre.append(char)
            try:
                pl = ("#" + dupre[0] + dupre[2] + dupre[4])
            except IndexError:
                pass
            else:
                for hexh in colorr:
                    try:
                        if len(exceptionprevent) > 0:
                            break
                        else:
                            if hexh[2] == pl:
                                exceptionprevent.append(hexh)
                                pi = exceptionprevent[0][2]
                                vi = exceptionprevent[0][1]
                                if len(self.colorw) - 1 > 5:
                                    self.colorw.pop()
                                self.colorw.append(pi)
                                if len(dupe) > 0:
                                    dupe.clear()
                                if len(hpz) > 0:
                                    hpz.clear()
                                if len(hdr) > 0:
                                    hdr.clear()
                                dupe.append(vi)
                                hpz.append(pi)
                                ui = str()
                                pbm = len(li)
                                for char in li:
                                    if pbm > 4:
                                        ui += char
                                if not ui:
                                    hdr.append(pi)
                                else:
                                    ups = ("#" + ui)
                                    hdr.append(ups)
                                    break
                    except IndexError:
                        pass
        try:
            exceptionprevent.clear()
        except IndexError:
            pass
        finally:
            if "#" not in pi:
                if not exceptionprevent:
                    try:
                        tryagain = webcolors.name_to_hex(pi)
                    except ValueError:
                        loser += 1
                        p = 0
                        hdr.append("#FF0000")
                    else:
                        if len(self.colorw) - 1 > 5:
                            self.colorw.pop()
                        self.colorw.append(pi)
                        p = len(self.colorw) - 1

            elif "#" in pi:
                if not exceptionprevent:
                    if len(self.colorw) - 1 > 5:
                        self.colorw.pop()
                    self.colorw.append(pi)
                    try:
                        if hdr[0] == pi:
                            if len(hdr) > 0:
                                hdr.clear()
                            hdr.append(pi)
                            p = len(self.colorw) - 1
                        else:
                            p = len(self.colorw) - 1
                    except IndexError:
                        if len(hdr) > 0:
                            hdr.clear()
                        hdr.append(pi)
                        p = len(self.colorw) - 1
            dupre.clear()

    # primes colors defined above this function (subclass) into a list of loopcolors (loopcolorw), and initiates the looping sequence
    def colorloop(self, colorloopen, loopbase):
        global loopss, p, ipn, iin, ipns, inf, rpn, ipx, looo, pail, hexy, wamp, spn
        ion = int(loopbase)
        wamp = 0
        iop = str(colorloopen)
        iops = iop.strip("#")
        de = str()
        fix = 0
        if "#" in iop:
            if not self.loopcolorwinfo:
                for hexe in colorr:
                    if hexe[2] == iop:
                        loose.append(hexe)
                try:
                    rpnn = str("red=" + loose[0][3])
                    rpnf = str("green=" + loose[0][4])
                    rpnd = str("blue=" + loose[0][5])
                    rpns = f"{rpnn},{rpnf},{rpnd}"
                    pail = loose[0][1]
                    pou = iop.upper()
                    self.loopcolorwinfo.extend([[pou, rpns, pail]])
                    colors.append(iop)
                except IndexError:
                    pass
                if loose:
                    pass
                elif not loose:
                    for char in iops:
                        loodup.append(char)
                    pts = str("#" + loodup[0] + loodup[2] + loodup[4])
                    for hexp in colorr:
                        if hexp[2] == pts:
                            loose.append(hexp)
                    try:
                        rpnn = str("red=" + loose[0][3])
                        rpnf = str("green=" + loose[0][4])
                        rpnd = str("blue=" + loose[0][5])
                        rpns = f"{rpnn},{rpnf},{rpnd}"
                        pail = loose[0][1]
                        pou = iop.upper()
                        self.loopcolorwinfo.extend([[pou, rpns, pail]])
                        colors.append(iop)
                    except IndexError:
                        pq = ""
                        requested_colour = webcolors.hex_to_rgb(iop)
                        pj = pq.join(str(requested_colour))
                        rpng = pj.replace("IntegerRGB", "").lstrip("(").rstrip(")").replace(" ", "")
                        pail = self.get_colour_name(requested_colour)
                        pou = iop.upper()
                        self.loopcolorwinfo.extend([[pou, rpng, pail]])
                        colors.append(iop)

            else:
                for hexd in colorr:
                    if hexd[2] == iop:
                        loose.append(hexd)
                try:
                    rpnn = str("red=" + loose[0][3])
                    rpnf = str("green=" + loose[0][4])
                    rpnd = str("blue=" + loose[0][5])
                    rpns = f"{rpnn},{rpnf},{rpnd}"
                    pail = loose[0][1]
                    self.loopcolorwinfo.extend([[colorloopen, rpns, pail]])
                    colors.append(iop)
                except IndexError:
                    pass
                if loose:
                    pass
                elif not loose:
                    for char in iops:
                        loodup.append(char)
                    pts = str("#" + loodup[0] + loodup[2] + loodup[4])
                    for hexp in colorr:
                        if hexp[2] == pts:
                            loose.append(hexp)
                    try:
                        rpnn = str("red=" + loose[0][3])
                        rpnf = str("green=" + loose[0][4])
                        rpnd = str("blue=" + loose[0][5])
                        rpns = f"{rpnn},{rpnf},{rpnd}"
                        pail = loose[0][1]
                        pou = iop.upper()
                        self.loopcolorwinfo.extend([[pou, rpns, pail]])
                        colors.append(iop)
                    except IndexError:
                        pq = ""
                        requested_colour = webcolors.hex_to_rgb(iop)
                        pj = pq.join(str(requested_colour))
                        rpng = pj.replace("IntegerRGB", "").lstrip("(").rstrip(")").replace(" ", "")
                        pail = self.get_colour_name(requested_colour)
                        pou = iop.upper()
                        self.loopcolorwinfo.extend([[pou, rpng, pail]])
                        colors.append(iop)
        else:
            if not self.loopcolorwinfo:
                rpn = iop.title()
                for nameu in colorr:
                    if nameu[1] == rpn:
                        loose.append(nameu)
                try:
                    hexy = loose[0][2]
                except IndexError:
                    try:
                        hexy = webcolors.name_to_hex(iop)
                    except ValueError:
                        print("Invalid loop color on one of specified colors, please try again")
                        wamp = 1
                    else:
                        rpn = ""
                        yup = str(hexy).upper()
                        looo = webcolors.hex_to_rgb(yup)
                        rr = rpn.join(str(looo))
                        rpnn = rr.replace("IntegerRGB", "").replace(" ", "").lstrip("(").rstrip(")")
                        self.loopcolorwinfo.extend([[yup, rpnn, iop]])
                        colors.append(hexy)
                else:
                    re = str(hexy).strip("#")
                    ro = len(re)
                    for char in re:
                        if ro < 4:
                            fix = 1
                            de += char + char
                    if fix == 1:
                        hexyp = ("#" + de)
                        hexy = hexyp
                    else:
                        pass
                    rpr = str("red=" + loose[0][3])
                    rpg = str("green=" + loose[0][4])
                    rpb = str("blue=" + loose[0][5])
                    looo = f"{rpr},{rpg},{rpb}"
                    self.loopcolorwinfo.extend([[hexy.upper(), looo, colorloopen]])
                    colors.append(hexy)
            else:
                rpn = iop.title()
                for namer in colorr:
                    if namer[1] == rpn:
                        loose.append(namer)
                try:
                    hexy = loose[0][2]
                except IndexError:
                    try:
                        hexy = webcolors.name_to_hex(iop)
                    except ValueError:
                        print("Invalid loop color on one of specified colors, please try again")
                        wamp = 1
                        ipn -= 1
                    else:
                        rpn = ""
                        yup = str(hexy).upper()
                        looo = webcolors.hex_to_rgb(yup)
                        rr = rpn.join(str(looo))
                        rpnn = rr.replace("IntegerRGB", "").replace(" ", "").lstrip("(").rstrip(")")
                        self.loopcolorwinfo.extend([[yup, rpnn, iop]])
                        colors.append(hexy)
                else:
                    re = str(hexy).strip("#")
                    ro = len(re)
                    for char in re:
                        if ro < 4:
                            fix = 1
                            de += char + char
                    if fix == 1:
                        hexyp = ("#" + de)
                        hexy = hexyp
                    else:
                        pass
                    rpr = str("red=" + loose[0][3])
                    rpg = str("green=" + loose[0][4])
                    rpb = str("blue=" + loose[0][5])
                    looo = f"{rpr},{rpg},{rpb}"
                    self.loopcolorwinfo.extend([[hexy.upper(), looo, colorloopen]])
                    colors.append(hexy)
        for item in loose:
            loose.clear()
        for item in loodup:
            loodup.clear()
        if ipn != ion:
            if wamp == 1:
                self.loopcolorwinfo.clear()
                self.lcancel()
                colors.clear()
                ipns = 1
                wamp = 0
            else:
                pass
        elif ipn == ion:
            ipn = 0
            u = 0
            for item in colors:
                self.loopcolorw.append(item)
            spn = len(self.loopcolorwinfo)
            colors.clear()
            if len(self.loopcolorw) > ion:
                for i in range(ipx):
                    self.loopcolorwinfo.pop(0)
                    self.loopcolorw.pop(0)
            ipx = ion
            loopss = 1
            if loopss == 0:
                if len(self.colorw) - 1 > 5:
                    p = len(self.colorw) - 1
                else:
                    try:
                        p = pi
                    except NameError:
                        pass

    def closest_hex_colour(self, requested_colour):
        min_colours = {}
        for key, nameu in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = nameu
        return min_colours[min(min_colours.keys())]

    def get_colour_name(self, requested_colour):
        try:
            closest_name = webcolors.rgb_to_name(requested_colour)
        except ValueError:
            closest_name = self.closest_hex_colour(requested_colour)
        return closest_name

    # defining a color you currently have equipped
    def colordef(self):
        global p, hexs, name, pe4, pe6, pe7, color, hexr, tehlel, wtfcolor, wtshit
        pe = str(self.colorw[p]).lower()
        try:
            # name
            pe4 = str(dupe[0])
            # 6 binary hex without "#"
            pe6 = str(hdr[0]).strip("#")
            # 6 binary hex
            pe7 = str(hdr[0]).upper()
        except IndexError:
            pe4 = self.colorw[p]
        if "#" in self.colorw[p]:
            try:
                # name
                pe4 = str(dupe[0])
            except IndexError:
                pass
            try:
                try:
                    if wtfcolor.startswith("#") and len(self.colorw[p]) > 4 or wtshit.startswith("#") and len(self.colorw[p]) > 4:
                        pe6 = self.colorw[p].strip("#")
                        pe7 = self.colorw[p].upper()
                    else:
                        # 6 binary hex without "#"
                        pe6 = str(hdr[0]).strip("#")
                        # 6 binary hex
                        pe7 = str(hdr[0]).upper()
                except NameError:
                    raise IndexError
            except IndexError:
                pe6 = str(self.colorw[p]).strip("#")
                pe7 = str(self.colorw[p]).upper()
            for hexp in colorr:
                if hexp[2] == pe:
                    sepe.append(hexp)
            if sepe:
                pass
            elif not sepe:
                for hexp in colorr:
                    if hexp[2] == pe:
                        sepe.append(hexp)
            try:
                if pe4 == sepe[0][1]:
                    color = sepe[0][1]
                else:
                    color = pe4
            except IndexError:
                requested_colour = webcolors.hex_to_rgb(self.colorw[p])
                pe4 = self.get_colour_name(requested_colour)
                color = pe4
            try:
                h = pe6
            except NameError:
                h = pe.lstrip("#")
            if p == 6:
                tehlel = f"Your color is: {pe7}\nColor ID: Custom\nRGB Values: " \
                             f"{tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))}\nColor Name: {color}"
            else:
                try:
                    o = self.colorw[p]
                    h = str(o).strip("#")
                    tehlel = f"Your color is: {self.colorw[p]}\nColor ID: {p}\nRGB Values: " \
                             f"{tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))}\nColor Name: {color}"
                except ValueError:
                    h = self.colorw[p]
                    tehlel = f"Your color is: {self.colorw[p]}\nColor ID: {p}\nRGB Values: " \
                             f"{tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))}\nColor Name: {color}"
        else:
            color = str(self.colorw[p]).title()
            try:
                pe6 = str(hdr[0])
            except IndexError:
                pe6 = webcolors.name_to_hex(color)
            for name in colorr:
                if name[1] == color:
                    sepe.append(name)
            try:
                hexs = sepe[0][2]
            except IndexError:
                hexs = webcolors.name_to_hex(pe)
                hexr = str(hexs).upper()
            h = hexs.lstrip("#")
            tehlel = f"Your color is: {hexr}\nColor ID: Custom\nRGB Values: " \
                     f"{tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))}\nColor Name: {color}"

        if sepe:
            for i in range(len(sepe)):
                sepe.clear()

    def loopdef(self):
        global tehlel
        tehlel = (tabulate(self.loopcolorwinfo, headers=self.loopcolorwheader,
                       tablefmt="simple", showindex=True))

    def lcancel(self):
        global ipn, ipns, err
        err += 1
        ipn = 0
        ipns = 1
        self.loopcolorw.clear()
        self.loopcolorwinfo.clear()
        colors.clear()

    # the function that allows you to move your character
    def control(self, radius, colory):
        global p, turtlw, loopss, loser
        turtle.pendown()
        turtle.speed("slowest")
        pgh = "#000000"
        if light == 0:
            turtle.bgcolor("black")
        elif light == 1:
            turtle.bgcolor("white")
        if loopss == 0:
            try:
                if light == 0:
                    turtle.pencolor(colory)
                    turtle.fillcolor(pgh)
                elif light == 1:
                    turtle.pencolor(colory)
                    turtle.fillcolor(colory)
            except turtle.TurtleGraphicsError:
                loser += 1
                p = 0
                self.colorw.pop()
        elif loopss == 1:
            try:
                if light == 0:
                    turtle.pencolor(colory)
                    turtle.fillcolor(pgh)
                elif light == 1:
                    turtle.pencolor(colory)
                    turtle.fillcolor(colory)
            except turtle.TurtleGraphicsError:
                loopss = 0
                print("Invalid loop color on one of specified colors, please try again")
        # turtle.left(90)
        forwards = keyboard.is_pressed("up")
        if forwards:
            turtle.forward(radius)
        lefty = keyboard.is_pressed("left")
        if lefty:
            turtle.left(5)
        righty = keyboard.is_pressed("right")
        if righty:
            turtle.right(5)
        backwards = keyboard.is_pressed("down")
        if backwards:
            turtle.backward(radius)
        if turtlw == 0:
            exit()

    # function that erases your art
    def reverse(self):
        global reset
        reset -= 1
        pain = turtle.pos()
        turtle.clear()
        self.sup()
        turtle.goto(pain)

    # the configuration of the font and the speed of turtle
    def text_at_xy(self, x, y, text):
        self.FONT = ("Arial", 14, "bold")
        if light == 0:
            turtle.pencolor("white")
        elif light == 1:
            turtle.pencolor("black")
        turtle.speed("fastest")
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(text, font=self.FONT)

    # prints the on-screen instructions and gets your character started
    def sup(self):
        self.text_at_xy(-300, 200, f"use arrow keys to move\n<--control panel")
        turtle.goto(0, -22)

    # go up
    def colorcontrolup(self):
        global p
        if p < len(self.colorw) - 1:
            p += 1
        else:
            p = 0

    # go down
    def colorcontroldown(self):
        global p
        if p > 0:
            p -= 1
        else:
            p = len(self.colorw) - 1

    # what gets the graphical interface going
    def man(self):
        global p, loopss, loser
        self.sup()
        while True:
            if loopss == 1:
                for colorq in self.loopcolorw:
                    if p < len(self.loopcolorw) - 1:
                        p += 1
                    else:
                        p = 0
                    self.control(sp, colorq)
            else:
                try:
                    self.control(sp, self.colorw[p])
                    if reset == 1:
                        self.reverse()
                    elif lost == 1:
                        begin()
                    elif lin == 1:
                        self.lightmode()
                except IndexError:
                    p = 0
                    print("Invalid hex or color name, please try again")


# starts the fun
if __name__ == "__main__":
    turtl = Turtle()
    p1 = threading.Thread(target=turtl.man)
    p2 = threading.Thread(target=network)
    p1.start()
    p2.start()
