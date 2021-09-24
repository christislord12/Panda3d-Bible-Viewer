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
        # text holding node
        self.TextHoldingNode = TextNode("node name")
        self.TextHoldingNode.setText("")
        self.TextHolder = aspect2d.attachNewNode(self.TextHoldingNode)
        self.TextHolder.reparentTo(render)
        self.TextHoldingNode.setTextColor(0,1,0,1)
        self.BookLoad("Dedicatory");
        # Camera
        base.useTrackball()
        base.trackball.node().setPos(-7.55,0,6)
        # Controls
        self.forward_button = KeyboardButton.up()
        self.backward_button = KeyboardButton.down()
        self.space_button = KeyboardButton.space()
        base.accept("escape",sys.exit)
        # movement speed
        self.forward_speed = 5.0 # units per second
        self.backward_speed = 2.0
        # UI
        menu = DirectOptionMenu(text="New", scale=0.04,items=["Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"],highlightColor=(0.65,0.65,0.65,1),command=self.BookLoad)
        menuold = DirectOptionMenu(text="Old", scale=0.04,items=["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","SongofSolomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi"],highlightColor=(0.65,0.65,0.65,1),command=self.BookLoad)
        menu.setPos(-1.31,0,0.8)
        menuold.setPos(-1.31,0,0.9)
        DownButton = DirectButton(text = (">"), scale=.15,command=self.GoDown)
        DownButton.setHpr(0,0,90)
        DownButton.setPos(-1.28,0,-0.9)
        UpButton = DirectButton(text = ("<"), scale=.15, command=self.GoUp)
        UpButton.setHpr(0,0,90)
        UpButton.setPos(1.24,0,-0.9)
        base.setBackgroundColor(1,1,1,1)
        # movement task
        taskMgr.add(self.MovementTask, "MyTaskName")
    def ClearText(self):
        self.TextHolder.removeNode()
        self.TextHoldingNode = TextNode("node name")
        self.TextHoldingNode.setText("")
        self.TextHolder = aspect2d.attachNewNode(self.TextHoldingNode)
        self.TextHolder.reparentTo(render)
        self.TextHoldingNode.setTextColor(0,0,0,1)
    def BookLoad(self,arg):
        self.ClearText()
        base.trackball.node().setPos(-7.55,0,6)
        textfile = open(str(arg) + ".txt")
        self.hi = 1
        for line in textfile.read().splitlines():
                self.text = TextNode("node name")
                self.text.setText(line)
                textNodePath = aspect2d.attachNewNode(self.text)
                textNodePath.setScale(0.44)
                textNodePath.setPos(0,30,self.hi)
                textNodePath.reparentTo(self.TextHolder)
                self.text.setTextColor(0,0,0,1)
                self.hi = self.hi - 0.5
    def GoDown(self):
        base.trackball.node().setPos(-7.55, 0, base.trackball.node().getZ() + 3)
    def GoUp(self):
        base.trackball.node().setPos(-7.55, 0, base.trackball.node().getZ() - 3)
    def MovementTask(self,task):
        base.trackball.node().setPos(-7.55, 0, base.trackball.node().getZ())
        base.trackball.node().setHpr(0, 0, 0)
        speed = 0.0
        is_down = base.mouseWatcherNode.is_button_down
        if is_down(self.forward_button):
            speed += self.forward_speed
            y_delta = -5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        if is_down(self.backward_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        if is_down(self.space_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        return task.cont
fgame = Game()
base.run()
