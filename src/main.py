from panda3d.core import loadPrcFileData
loadPrcFileData("", "win-size 800 600")
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.task import Task
from direct.showbase.DirectObject import DirectObject
import sys
class Game(DirectObject):
    def __init__(self):
        base = ShowBase()
        self.text = TextNode("node name")
        self.BibleTextFileName = "eng-kjv2006_vpl.txt"
        self.CurrentBibleBook = "" 
        # init text
        self.textNodePath = aspect2d.attachNewNode(self.text)
        self.textNodePath.setScale(0.11)
        self.textNodePath.setPos(0,0,0)
        self.text.setTextColor(0,0,0,1)
       # base.setBackgroundColor(1,1,1)
        self.text.setWordwrap(30)
        # new menu stuff
        self.BibleBookListFrame = DirectScrolledFrame(canvasSize=(0, 0, -7, 7), frameSize=(-.1, .2, -1.5, 1.5))
        self.BibleBookListFrame.setPos(-1.2, 0, -0)
        self.BibleBookListFrame.setScale(0.6)
        #load the books into the menu
        self.LoadBibleBookMenu()
        #Bible Frame
        #initialize it so it can be used as a variable
        self.BibleFrame = DirectScrolledFrame()
        #load up the bible frame
        self.LoadBibleFrame()
        # Chapter menu
        self.BibleChapterMenu = DirectScrolledFrame()
        # Load John 1
        self.LoadBibleBook("JOH",1)
    def LoadBibleFrame(self):
        self.BibleFrame.removeNode()
        self.BibleFrame = DirectScrolledFrame(canvasSize=(0, 0, -20, 20), frameSize=(-1.7, 1.7, -1.5, 1.5))
        #self.BibleFrame.setPos(-1.2, 0, -0)
        self.BibleFrame.setScale(0.6)
        self.textNodePath.setPos(-0,0,19.9)
        self.textNodePath.reparentTo(self.BibleFrame.getCanvas())
    def LoadBibleBookMenu(self):
        origlist = [] 
        textfile = open(self.BibleTextFileName)
        for line in textfile:
                linestring = line[:4]
                origlist.append(linestring)
                #print linestring
        resultlist = [] 
        for i in origlist: 
                 if i not in resultlist: 
                      resultlist.append(i)
        zoffset = 6.9          
        for book in resultlist:
            l = DirectButton(text=book, scale=.1, command=self.LoadBibleBook,extraArgs=[book,1])
            l.setZ(zoffset)
            zoffset = zoffset -0.13
            l.setX(0.1)
            l.reparentTo(self.BibleBookListFrame.getCanvas())
    def LoadChapterMenu(self, arg):
        self.BibleChapterMenu.removeNode()
        self.BibleChapterMenu = DirectScrolledFrame(canvasSize=(0, 0, -10, 10), frameSize=(-.1, .2, -1.5, 1.5))
        self.BibleChapterMenu.setPos(1.2, 0, -0)
        self.BibleChapterMenu.setScale(0.6)
        textfile = open(self.BibleTextFileName)
        for line in textfile:
             if line.startswith(str(arg)):
                 pass
                 last_line = line
        new = last_line.split(":")
        # print new[0]
        newstring = new[0]
        finalnumstr = newstring[4:]
        self.chapternumber = int(finalnumstr)
        zoffset = 9.9         
        for x in range(self.chapternumber + 1):
            if x != 0:
                l = DirectButton(text=str(x), scale=.1, command=self.LoadBibleBook,extraArgs=[arg.strip(),x])
                l.setZ(zoffset)
                zoffset = zoffset -0.13
                l.setX(0.1)
                l.reparentTo(self.BibleChapterMenu.getCanvas())
    def LoadBibleBook(self,arg,chapter):
        #reload Bible frame. 
        self.LoadBibleFrame()
        # set chapter number to 1
        self.LoadChapterMenu(arg)
        booktext = ""
        textfile = open(self.BibleTextFileName)
        for line in textfile:
            if line.startswith(str(arg.strip()) + " " + str(chapter) +":"):
                   #remove VPL prefix
                   booktext = booktext + line[4:] 
        self.text.setText(booktext)
fgame = Game()
base.run()