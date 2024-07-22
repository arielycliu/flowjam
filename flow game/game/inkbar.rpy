screen inkbar:
    bar:
        value ink
        range 100
        left_bar "gui/bar/idle_bar.png"
        right_bar "gui/bar/empty_bar.png"
        thumb "gui/bar/thumb_bar_ink.png"
        thumb_offset 9
        xysize(432, 150)
        xalign 0.08
        yalign 0.02

label ink_demo:
    "Show ink"

    show screen inkbar
    $ ink = 0
    while ink < 100:
        $ ink += 1
        pause(0.0001)
    "demo 100"

    while ink != 50:
        if ink > 50:
            $ ink -= 1
        else:
            $ ink += 1
        pause(0.0001)
    "demo 50"

    while ink != 70:
        if ink > 70:
            $ ink -= 1
        else:
            $ ink += 1
        pause(0.0001)
    "demo 70"

    $ goal = 20
    while ink != goal:
        if ink > goal:
            $ ink -= 1
        else:
            $ ink += 1
        pause(0.0001)
    "demo [goal]"

    jump timeline_demo