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
    hide screen inkbar
    hide screen notebook_display_toggle
    hide screen notebook_menu
    hide elias
    hide synthea
    hide toshi
    hide peregrine
    call screen TimelineUI


screen TimelineUI:
    add "Timeline/timeline.png"

    # Gap of 344 between major nodes
    # Gap of 86.25 between smaller nodes: 86, 87, 86

    # ypos is always 515
    default part1_xpos = [2000, 249, 335, 422, 508]  # first position is if we want to hide the timeline btn
    default part2_xpos = [2000, 593, 679, 766, 852]
    default part3_xpos = [2000, 937, 1015, 1101, 1188]
    default part4_xpos = [2000, 1281, 1359, 1445, 1532]
    default complete = True if part1 == part2 == part3 == part4 == 4 else False

    default xpos1 = part1_xpos[part1]
    default xpos2 = part2_xpos[part2]
    default xpos3 = part3_xpos[part3]
    default xpos4 = part4_xpos[part4]
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

label timeline_pressed1:
    if part1 == 1:
        jump toshi1
    elif part1 == 2:
        jump toshi2
    elif part1 == 3:
        jump toshi3
    elif part1 == 4:
        jump toshi4

label timeline_pressed2:
    if part2 == 1:
        jump peregrine1
    elif part2 == 2:
        jump peregrine2
    elif part2 == 3:
        jump peregrine3
    elif part2 == 4:
        jump peregrine4


label timeline_pressed3:
    if part3 == 1:
        jump nostro1
    elif part3 == 2:
        jump nostro2
    elif part3 == 3:
        jump nostro3
    elif part3 == 4:
        jump nostro4

label timeline_pressed4:
    if part4 == 1:
        jump synthea1
    elif part4 == 2:
        jump synthea2
    elif part4 == 3:
        jump synthea3
    elif part4 == 4:
        jump synthea4


label timeline_pressed_final:
    jump game_end


