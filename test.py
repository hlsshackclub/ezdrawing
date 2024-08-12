import ezdrawing

ezdrawing.open_window((100, 100))

ezdrawing.draw_rect((0, 0, 0), (50, 100), (300, 300))

while not ezdrawing.should_quit():
    ezdrawing.undo()
    ezdrawing.draw_line((0, 0, 0), (0, 0), ezdrawing.get_mouse_pos(), 25)
    ezdrawing.update()
ezdrawing.quit()