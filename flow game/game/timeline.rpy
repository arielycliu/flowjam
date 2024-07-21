## Screen with Stats Button
screen timelineButton:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "gui/button/timeline_%s.png"
        action Jump ("call_timelineUI")

label call_timelineUI:
    define part1 = 4
    define part2 = 4
    define part3 = 4
    define part4 = 4
    call screen TimelineUI


screen TimelineUI:
    add "Timeline/timeline.png"

    # Gap of 344 between major nodes
    # Gap of 86.25 between smaller nodes: 86, 87, 86

    # ypos is always 515
    default part1_xpos = [249, 335, 422, 508]
    default part2_xpos = [593, 679, 766, 852]
    default part3_xpos = [937, 1015, 1101, 1188]
    default part4_xpos = [1281, 1359, 1445, 1532]
    default complete = True if part1 == part2 == part3 == part4 == 4 else False

    default xpos1 = part1_xpos[part1 - 1]
    default xpos2 = part2_xpos[part2 - 1]
    default xpos3 = part3_xpos[part3 - 1]
    default xpos4 = part4_xpos[part4 - 1]
    default xposfinal = 1618 if complete else 2500

    imagebutton:
        xpos xpos1
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("timeline_pressed1")
        
    imagebutton:
        xpos xpos2
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("timeline_pressed2")
    
    imagebutton:
        xpos xpos3
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("timeline_pressed3")
    
    imagebutton:
        xpos xpos4
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("timeline_pressed4")

    imagebutton:
        xpos xposfinal
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("timeline_pressed_final")

label timeline_demo:
    show screen timelineButton
    "The timeline button is apprearing."
    "test2"
    return

label timeline_pressed_final:
    jump game_end


