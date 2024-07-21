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
    call screen TimelineUI



define part1_xpos = [249, 335, 422, 508]
define part2_xpos = [593, 679, 766, 852]
define part3_xpos = [937, 1015, 1101, 1188]
define part4_xpos = [1281, 1359, 1445, 1532]


screen TimelineUI:
    add "Timeline/timeline.png"

    # Gap of 344 between major nodes
    # Gap of 86.25 between smaller nodes: 86, 87, 86

    # ypos is always 515
    default part1 = 4
    default part2 = 4
    default part3 = 4
    default part4 = 4
    default complete = True

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
        action Jump("house1_pressed")
        
    imagebutton:
        xpos xpos2
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("house1_pressed")
    
    imagebutton:
        xpos xpos3
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("house1_pressed")
    
    imagebutton:
        xpos xpos4
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("house1_pressed")

    imagebutton:
        xpos xposfinal
        ypos 515
        idle "Timeline/node_idle.png"
        hover "Timeline/node_hover.png"
        action Jump("house1_pressed")

label timeline_demo:
    # use the code below to show the "map" button
    show screen timelineButton
    "The timeline button is apprearing."
    "test2"
    return

label house1_pressed:
    scene bg classroom
    "House 1 was pressed!"
    jump after_house_choice

label house2_pressed:
    "House 2 was pressed!"
    jump after_house_choice


label after_house_choice:
    "Tada!"
    return