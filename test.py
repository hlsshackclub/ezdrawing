import ezdrawing

ezdrawing.open_window((800, 800))

tool_in_use = "pen"
def selectTool():
    global tool_in_use
    pressed_keys = ezdrawing.get_pressed_keys()
    if "1" in pressed_keys:
        tool_in_use = "pen"
    elif "2" in pressed_keys:
        tool_in_use = ""

last_mouse_pos = (0, 0)
while not ezdrawing.should_quit():
    selectTool()
    
    
    #
    mouse_pos = ezdrawing.get_mouse_pos()
    if 1 in ezdrawing.get_pressed_mouse_buttons():
        ezdrawing.draw_capped_line((0, 0, 0), last_mouse_pos, mouse_pos, 10)
    
    last_mouse_pos = mouse_pos
    
    ezdrawing.update()
ezdrawing.quit()