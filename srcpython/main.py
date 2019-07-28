from panda3d.core import loadPrcFileData
loadPrcFileData("", "sync-video t")
loadPrcFileData("", "show-frame-rate-meter f")
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
        textfile = open("Dedicatory.txt")
        self.text.setText(textfile.read())
        textNodePath = aspect2d.attachNewNode(self.text)
        textNodePath.setScale(0.5)
        textNodePath.setPos(0,30,0)
        textNodePath.reparentTo(render)
        self.text.setTextColor(0,0,0,1)
        base.setBackgroundColor(1,1,1)
        #font = loader.loadFont("tnr.bam")
        #font.setPixelsPerUnit(25)
        self.text.setWordwrap(35)
        #self.text.setFont(font)
        base.accept("escape",sys.exit)
        base.useTrackball()
        self.output = "Psalms.txt"
        base.trackball.node().setPos(-7.55,0,6)
        menu = DirectOptionMenu(text="New", scale=0.04,items=["Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"],highlightColor=(0.65,0.65,0.65,1),command=self.itemSel)
        menuold = DirectOptionMenu(text="Old", scale=0.04,items=["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","SongofSolomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi"],highlightColor=(0.65,0.65,0.65,1),command=self.itemSel)
        menu.setPos(-1.31,0,0.8)
        menuold.setPos(-1.31,0,0.9)
        onebutton = DirectButton(text = ("NextSection"), scale=.04, command=self.one)
        onebutton.setPos(-1.2,0,0.7)
        self.sectnum=1
        taskMgr.add(self.exampleTask, "MyTaskName")
    def read_in_chunks(self,file_object, chunk_size=50000):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data
    def itemSel(self,arg):
        self.sectnum=2
        self.text.setText("")
        base.trackball.node().setPos(-7.55,0,6)
        self.output = arg+".txt"
        f = open(self.output)
        for piece in self.read_in_chunks(f):
            self.text.setText(piece)
            return
    def one(self):
        currentnum=1
        self.sectnum=self.sectnum+1
        self.text.setText("")
        base.trackball.node().setPos(-7.55,0,6)
        f = open(self.output)
        for piece in self.read_in_chunks(f):
            self.text.setText("")
            currentnum=currentnum+1
            self.text.setText(piece)
            if self.sectnum == currentnum:
                return
    def exampleTask(self,task):
        base.trackball.node().setPos(-7.55, 0, base.trackball.node().getZ())
        base.trackball.node().setHpr(0, 0, 0)
        return task.cont
fgame = Game()
base.run()
