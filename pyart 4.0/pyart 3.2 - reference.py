import tkinter as tk
import turtle
import keyboard
import webcolors
from tabulate import tabulate
import csv
import sys
import os

# modules to install: keyboard, webcolors, tabulate

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

# the master frame of tkinter (control interface)
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.contents = tk.StringVar()
        self.contentss = tk.StringVar()
        self.entrythingy = tk.Entry()
        self.master.maxsize(500, 500)
        self.master.geometry("235x150")
        self.master = master
        self.pack()


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

# saves the 6 binary hexes
hdr = []

# keeps track so it can know what to append to loopcolorw
colors = []

# 0 = dark theme, 1 = light theme
light = 0


# reset function
def begin():
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, -22)
    turtle.speed("slowest")
    turtle.pendown()


# prints the color definitions
def colord():
    print("0 = Red\n1 = Yellow\n2 = Green\n3 = Cyan\n4 = Blue\n5 = Magenta\n\n" +
          "NOTICE: Custom colors defined will be erased upon doing this command")


# quits the program
def quitsd():
    global turtlw
    turtlw = 0

# changelog
def change():
    print("History of versions: \n\nPyArt 3.2: More bug fixes, speed now integrated to Tkinter interface, fixed certain "
          "color names not showing color details when pressed \"What is my \ncolor?\". "
          "\n\nPyArt 3.1.1: Added ability to adjust length of movement. "
          "\n\nPyArt 3.1: Enhanced color interpreting definition library, added light theme, and shows you an indication "
          "when you change your color with the \ncolor+ and color- buttons printing color pid with visual indication. "
          "\n\nPyArt 3.0: Added color looping function, and reorganized the buttons. "
          "\n\nPyArt 2.1: Various bug fixing, integrated the quit button to the tkinter interface + integrated a foreshadow "
          "feature in defining hexes (shhh), and\nmade the predefined color definitions easier to comprehend through visuals. "
          "\n\nPyArt 2.0: Added buttons to the side, now able to move colors up and down, and change to defined color, or "
          "change to a hex or name of color. "
          "\n\nPyArt 1.0: a way to move your character with arrow keys, and using keyboard to restart, move your character,"
          " or quit program. \n\nNewer versions found in: "
          "https://drive.google.com/drive/folders/1yb-VcgXpkmF9ULQyUolACCkNuEoNAzpO?usp=sharing")


# the pyart app
class Turtle(Application):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        with open(csvi, "r", newline="") as csi:
            readi = csv.reader(csi)
            for row in readi:
                colorr.append(row)
        self.create_widgets()

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

    # buttons of interface
    def create_widgets(self):
        self.reset = tk.Button(self, text="reset", command=self.reverse)
        self.reset.grid(row=1, column=3)
        self.channelup = tk.Button(self, text="+Color", command=self.colorcontrolup)
        self.channelup.grid(row=3, column=3)
        self.channeldown = tk.Button(self, text="-Color", command=self.colorcontroldown)
        self.channeldown.grid(row=4, column=3)
        self.go = tk.Button(self, text="Lost", command=begin)
        self.go.grid(row=2, column=3)
        self.colordefiner = tk.Button(self, text="Predefined color", command=self.colorno)
        self.colordefiner.grid(row=1, column=2)
        self.customcolor = tk.Button(self, text="Custom color", command=self.colornohex)
        self.customcolor.grid(row=2, column=2)
        self.getcolor = tk.Button(self, text="What is my color?", command=self.colordef)
        self.getcolor.grid(row=4, column=2)
        self.loopsd = tk.Button(self, text="Define color loop", command=self.loo)
        self.loopsd.grid(row=3, column=2)
        self.quitd = tk.Button(self, text="quit", command=quitsd)
        self.quitd.grid(row=7, column=2)
        self.chag = tk.Button(self, text="changelog", command=change)
        self.chag.grid(row=7, column=1)
        if light == 0:
            self.lit = tk.Button(self, text="Light Theme", command=self.lyght)
        elif light == 1:
            self.lit = tk.Button(self, text="Dark Theme", command=self.dpark)
        self.lit.grid(row=2, column=1)
        self.speed = tk.Button(self, text="Speed+", command=self.spine)
        self.speed.grid(row=3, column=1)
        self.slow = tk.Button(self, text="Speed-", command=self.spike)
        self.slow.grid(row=4, column=1)
        self.tr = tk.Label(self, text=f"Speed: {sp}")
        self.tr.grid(row=1, column=1)


    def loopwidgets(self):
        self.reset = tk.Button(self, text="reset", command=self.reverse)
        self.reset.grid(row=3, column=1)
        self.go = tk.Button(self, text="Lost", command=begin)
        self.go.grid(row=4, column=1)
        self.colordefiner = tk.Button(self, text="Predefined color", command=self.colorno)
        self.colordefiner.grid(row=1, column=2)
        self.customcolor = tk.Button(self, text="Custom color", command=self.colornohex)
        self.customcolor.grid(row=2, column=2)
        self.getcolor = tk.Button(self, text="What is my color?", command=self.loopdef)
        self.getcolor.grid(row=4, column=2)
        self.loopsd = tk.Button(self, text="Define color loop", command=self.loo)
        self.loopsd.grid(row=3, column=2)
        self.quitd = tk.Button(self, text="quit", command=quitsd)
        self.quitd.grid(row=5, column=2)
        self.speed = tk.Button(self, text="Speed+", command=self.loospine)
        self.speed.grid(row=1, column=3)
        self.slow = tk.Button(self, text="Speed-", command=self.loospike)
        self.slow.grid(row=2, column=3)
        self.chag = tk.Button(self, text="changelog", command=change)
        self.chag.grid(row=5, column=1)
        if light == 0:
            self.lit = tk.Button(self, text="Light Theme", command=self.lyght)
        elif light == 1:
            self.lit = tk.Button(self, text="Dark Theme", command=self.dpark)
        self.lit.grid(row=2, column=1)
        self.tr = tk.Label(self, text=f"Speed: {sp}")
        self.tr.grid(row=1, column=1)

    # increases the length of movement (50 is max)
    def spine(self):
        global sp
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        if sp == 50:
            pass
        else:
            sp += 5
        self.create_widgets()

    def loospine(self):
        global sp
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        if sp == 50:
            pass
        else:
            sp += 5
        self.loopwidgets()

    # decreases the length of movement (10 is min)
    def spike(self):
        global por
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        if sp == 10:
            pass
        else:
            sp -= 5
        self.create_widgets()

    def loospike(self):
        global por
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        if sp == 10:
            pass
        else:
            sp -= 5
        self.loopwidgets()

    # light mode
    def lyght(self):
        global light
        light = 1
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        pin = turtle.pos()
        self.sup()
        turtle.goto(pin)
        if loopss == 0:
            self.create_widgets()
        elif loopss == 1:
            self.loopwidgets()

    # dark mode
    def dpark(self):
        global light
        light = 0
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        pin = turtle.pos()
        self.sup()
        turtle.goto(pin)
        if loopss == 0:
            self.create_widgets()
        elif loopss == 1:
            self.loopwidgets()

    # defining a number of colors to loop through
    def loo(self):
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        self.show = tk.Label(text="Enter the number of colors to loop to:")
        self.show.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind("<Key-Return>", self.colorentry)
        if loopss == 0:
            self.cancelc = tk.Button(self, text="Cancel", command=self.ccancel)
        elif loopss == 1:
            self.cancelc = tk.Button(self, text="Cancel", command=self.looccancel)
        self.cancelc.pack()

    def colorno(self):
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        self.show = tk.Label(text="Enter the color number(0-5):")
        self.show.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.colorno2)
        if loopss == 0:
            self.cancelc = tk.Button(self, text="Cancel", command=self.cancel)
        elif loopss == 1:
            self.cancelc = tk.Button(self, text="Cancel", command=self.loocancel)
        self.cancelc.pack(side="bottom")
        self.definition = tk.Button(self, text="Color def", fg=self.colorw[p], command=colord)
        self.definition.pack(side="top")

    def colornohex(self):
        self.reset.destroy()
        self.channelup.destroy()
        self.channeldown.destroy()
        self.go.destroy()
        self.colordefiner.destroy()
        self.customcolor.destroy()
        self.getcolor.destroy()
        self.quitd.destroy()
        self.loopsd.destroy()
        self.chag.destroy()
        self.lit.destroy()
        self.speed.destroy()
        self.slow.destroy()
        self.tr.destroy()
        self.show = tk.Label(text="Enter the hex or color name:")
        self.show.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.ap)
        if loopss == 0:
            self.cancelc = tk.Button(self, text="Cancel", command=self.ccancel)
        elif loopss == 1:
            self.cancelc = tk.Button(self, text="Cancel", command=self.looccancel)
        self.cancelc.pack()

    # predefined colors setup
    def colorno2(self, event):
        global p, pi, loopss
        if loopss == 1:
            loopss = 0
        try:
            pi = int(self.contents.get())
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
            for i in range(len(self.colorw) - 1):
                if i > 4:
                    self.colorw.pop()
        self.entrythingy.destroy()
        self.show.destroy()
        self.definition.destroy()
        self.cancelc.destroy()
        self.create_widgets()
        try:
            return pi
        except NameError:
            pass
        self.entrythingy.destroy()
        self.show.destroy()
        self.definition.destroy()
        self.cancelc.destroy()
        self.create_widgets()

    # custom hex color setup
    def ap(self, event):
        global p, pl, pf, pi, ui, loopss
        pi = str(self.contents.get())
        if loopss == 1:
            loopss = 0
        if "#" in pi:
            pi = str(self.contents.get())
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
            pi = str(self.contents.get()).title()
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
            pi = str(self.contents.get())
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
                        webcolors.name_to_hex(pi)
                    except ValueError:
                        p = 0
                        hdr.append("#FF0000")
                        print("Invalid hex or color name, please try again")
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
            self.show.destroy()
            self.entrythingy.destroy()
            self.cancelc.destroy()
            self.create_widgets()
            dupre.clear()

    # entering in as many colors as the number defines it
    def colorentry(self, event):
        global loopss, colorpw, ipn, io, ipns
        self.entrythingy.destroy()
        self.show.destroy()
        self.cancelc.destroy()
        try:
            io = int(self.contents.get())
        except ValueError:
            io = 0
            print("Invalid base number of loops, please try again")
            if loopss == 0:
                self.ccancel()
            elif loopss == 1:
                self.looccancel()
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
            if ipns == 1:
                self.show = tk.Label(text="Enter in 1 more color:")
            else:
                self.show = tk.Label(text=f"Enter in {ipns} more colors:")
            self.show.pack()
            self.entrythingy2 = tk.Entry()
            self.entrythingy2.pack()
            self.entrythingy2["textvariable"] = self.contentss
            self.entrythingy2.bind("<Key-Return>", self.colorloop)
            if loopss == 0:
                self.cancelc = tk.Button(self, text="Cancel", command=self.lcancel)
            else:
                self.cancelc = tk.Button(self, text="Cancel", command=self.loolcancel)
            self.cancelc.pack()

    # primes colors defined above this function (subclass) into a list of loopcolors (loopcolorw), and initiates the looping sequence
    def colorloop(self, event):
        global loopss, p, ipn, iin, ipns, inf, rpn, ipx, looo, pail, hexy, wamp, spn
        ion = int(self.contents.get())
        wamp = 0
        self.show.destroy()
        self.entrythingy2.destroy()
        self.cancelc.destroy()
        iop = str(self.contentss.get())
        iops = str(self.contentss.get()).strip("#")
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
                    pou = str(self.contentss.get()).upper()
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
                        pou = str(self.contentss.get()).upper()
                        self.loopcolorwinfo.extend([[pou, rpns, pail]])
                        colors.append(iop)
                    except IndexError:
                        pq = ""
                        requested_colour = webcolors.hex_to_rgb(iop)
                        pj = pq.join(str(requested_colour))
                        rpng = pj.replace("IntegerRGB", "").lstrip("(").rstrip(")").replace(" ", "")
                        pail = self.get_colour_name(requested_colour)
                        pou = str(self.contentss.get()).upper()
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
                    self.loopcolorwinfo.extend([[self.contentss.get(), rpns, pail]])
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
                        pou = str(self.contentss.get()).upper()
                        self.loopcolorwinfo.extend([[pou, rpns, pail]])
                        colors.append(iop)
                    except IndexError:
                        pq = ""
                        requested_colour = webcolors.hex_to_rgb(iop)
                        pj = pq.join(str(requested_colour))
                        rpng = pj.replace("IntegerRGB", "").lstrip("(").rstrip(")").replace(" ", "")
                        pail = self.get_colour_name(requested_colour)
                        pou = str(self.contentss.get()).upper()
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
                    self.loopcolorwinfo.extend([[hexy.upper(), looo, self.contentss.get()]])
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
                    self.loopcolorwinfo.extend([[hexy.upper(), looo, self.contentss.get()]])
                    colors.append(hexy)
        for item in loose:
            loose.clear()
        for item in loodup:
            loodup.clear()
        if ipn != ion:
            if wamp == 1:
                if loopss == 1:
                    for item in self.loopcolorwinfo:
                        if len(self.loopcolorwinfo) > spn:
                            self.loopcolorwinfo.pop()
                        else:
                            pass
                    for i in range(ipx):
                        if len(self.loopcolorw) > ipx:
                            self.loopcolorw.pop()
                        else:
                            pass
                    colors.clear()
                    self.loolcancel()
                    ipns = 1
                    wamp = 0
                elif loopss == 0:
                    self.loopcolorwinfo.clear()
                    self.lcancel()
                    colors.clear()
                    ipns = 1
                    wamp = 0
            else:
                self.colorentry(None)
        elif ipn == ion:
            loopss = 1
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
            self.loopwidgets()
            while loopss == 1:
                for colorq in self.loopcolorw:
                    if p < len(self.loopcolorw) - 1:
                        p += 1
                    else:
                        p = 0
                    self.control(sp, colorq)
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
        global p, hexs, name, pe4, pe6, pe7, color, hexr
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
            # 6 binary hex without "#"
            try:
                pe6 = str(hdr[0]).strip("#")
                # 6 binary hex
                pe7 = str(hdr[0]).upper()
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
                print("Your color is: " + pe7, "\nColor ID: Custom\nRGB Values:",
                      tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), "\nColor Name:", color)

            else:
                try:
                    o = self.colorw[p]
                    h = str(o).strip("#")
                    print("Your color is: " + self.colorw[p], "\nColor ID:", p, "\nRGB Values:",
                          tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), "\nColor Name:", color)
                except ValueError:
                    h = self.colorw[p]
                    print("Your color is: " + self.colorw[p], "\nColor ID:", p, "\nRGB Values:",
                          tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), "\nColor Name:", color)
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

            print("Your color is: " + hexr, "\nColor ID: Custom\nRGB Values:",
                  tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), "\nColor Name:", color)
        if sepe:
            for i in range(len(sepe)):
                sepe.clear()

    def loopdef(self):
        print(tabulate(self.loopcolorwinfo, headers=self.loopcolorwheader,
                       tablefmt="simple", showindex=True))

    # cancel and ccancel are what drops back to main control
    def ccancel(self):
        self.show.destroy()
        self.entrythingy.destroy()
        self.cancelc.destroy()
        self.create_widgets()

    def looccancel(self):
        self.show.destroy()
        self.entrythingy.destroy()
        self.cancelc.destroy()
        self.loopwidgets()

    def lcancel(self):
        global ipn, ipns
        self.show.destroy()
        self.entrythingy.destroy()
        self.entrythingy2.destroy()
        self.cancelc.destroy()
        self.create_widgets()
        ipn = 0
        ipns = 1
        self.loopcolorw.clear()
        self.loopcolorwinfo.clear()
        colors.clear()

    def loolcancel(self):
        global ipn, ipns
        self.show.destroy()
        self.entrythingy.destroy()
        self.entrythingy2.destroy()
        self.cancelc.destroy()
        self.loopwidgets()
        ipn = 0
        ipns = 1
        self.loopcolorw.clear()
        self.loopcolorwinfo.clear()
        colors.clear()

    def cancel(self):
        self.show.destroy()
        self.entrythingy.destroy()
        self.cancelc.destroy()
        self.definition.destroy()
        self.create_widgets()

    def loocancel(self):
        self.show.destroy()
        self.entrythingy.destroy()
        self.cancelc.destroy()
        self.definition.destroy()
        self.loopwidgets()

    # the function that allows you to move your character
    def control(self, radius, colory):
        global p, turtlw, loopss
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
                p = 0
                self.colorw.pop()
                print("Invalid hex or color name, please try again")
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
        self.text_at_xy(-300, 200, "use arrow keys to move\n<--control panel")
        turtle.goto(0, -22)

    # go up
    def colorcontrolup(self):
        global p
        for i in range(len(self.colorw) - 1):
            if i > 4:
                self.colorw.pop()
                p = 0
        if p < len(self.colorw) - 1:
            p += 1
        else:
            p = 0
        if p == 0:
            print(f"Color 0")
        elif p == 1:
            print(f"Color 1")
        elif p == 2:
            print(f"Color 2")
        elif p == 3:
            print(f"Color 3")
        elif p == 4:
            print(f"Color 4")
        elif p == 5:
            print(f"Color 5")

    # go down
    def colorcontroldown(self):
        global p
        for i in range(len(self.colorw) - 1):
            if i > 4:
                self.colorw.pop()
        if p > 0:
            p -= 1
        else:
            p = 5
        if p == 0:
            print(f"Color 0")
        elif p == 1:
            print(f"Color 1")
        elif p == 2:
            print(f"Color 2")
        elif p == 3:
            print(f"Color 3")
        elif p == 4:
            print(f"Color 4")
        elif p == 5:
            print(f"Color 5")

    # what gets the graphical interface going
    def man(self):
        global p, loopss
        self.sup()
        while True:
            if loopss == 1:
                self.control(sp, self.loopcolorw[p])
            else:
                try:
                    self.control(sp, self.colorw[p])
                except IndexError:
                    p = 0
                    print("Invalid hex or color name, please try again")


# starts the fun
if __name__ == "__main__":
    turtl = Turtle()
    turtl.man()
    turtl.mainloop()
