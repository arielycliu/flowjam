# Screen with Stats Button
screen timelineButton:
    imagebutton:
        xalign 0.95
        yalign 0.08
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

    imagebutton:
        xalign 0.95
        yalign 0.08
        xoffset -30
        yoffset 30
        auto "gui/button/close_%s.png"
        action Rollback()

    # Gap of 344 between major nodes
    # Gap of 86.25 between smaller nodes: 86, 87, 86

    # ypos is always 515
    default part1_xpos = [2000, 252, 338, 425, 511]  # first position is if we want to hide the timeline btn
    default part2_xpos = [2000, 596, 682, 769, 855]
    default part3_xpos = [2000, 940, 1018, 1104, 1191]
    default part4_xpos = [2000, 1284, 1362, 1448, 1535]
    default complete = True if part1 == part2 == part3 == part4 == 4 else False

    default xpos1 = part1_xpos[part1]
    default xpos2 = part2_xpos[part2]
    default xpos3 = part3_xpos[part3]
    default xpos4 = part4_xpos[part4]
    default xposfinal = 1621 if complete else 2500

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
    jump expression toshi_bookmark

label timeline_pressed2:
    jump expression peregrine_bookmark

label timeline_pressed3:
    jump expression nostro_bookmark

label timeline_pressed4:
    jump expression synthea_bookmark

label timeline_pressed_final:
    jump game_end


