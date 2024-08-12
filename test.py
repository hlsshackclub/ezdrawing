import ezdrawing

ezdrawing.open_window((100, 100))

ezdrawing.draw_rect((0, 0, 0), (50, 100), (300, 300))

while not ezdrawing.should_quit():
    ezdrawing.undo()
    ezdrawing.draw_text("hii", "arial", 20, ezdrawing.get_mouse_pos(), (0, 0, 0))
    ezdrawing.update()
ezdrawing.quit()