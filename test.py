import ezdrawing

ezdrawing.openWindow((100, 100))

ezdrawing.drawRect((0, 0, 0), (50, 100), (300, 300))

while not ezdrawing.shouldQuit():
    ezdrawing.undo()
    ezdrawing.drawLine((0, 0, 0), (0, 0), ezdrawing.getMousePos(), 25)
    ezdrawing.update()
ezdrawing.quit()