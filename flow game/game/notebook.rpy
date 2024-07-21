screen notebook_display_toggle:
    zorder 92
    imagebutton:
        idle "gui/button/notebookbutton_idle.png"
        hover "gui/button/notebookbutton_hover.png"
        action ToggleScreen("notebook_item_description")
        xalign 0.05
        yalign 0.1

    on "hide" action Hide("notebook_item_description")


default notebook_items = []
default current_item = ""

style inv_button is frame:
    xminimum 100
    ysize 100
    xpadding 50

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen notebook_item_description:
    # modal True  # controls if you can read dialogue and look at notebook at the same time
    window:
        background "#4f39284a"
        xsize 1290
        ysize 500
        xalign 0.5
        yalign 0.4
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in notebook_items:
                textbutton item:
                    action SetVariable("current_item", item)
                    selected False


label notebook_test:   

    "Hello {font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}darling ~{/b}{/size}{/font}."

    show screen notebook_display_toggle
    "See that notebook button?"

    "Let's add a phrase to it. How about {font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}As the ink flows{/b}{/size}{/font}?"
    $ notebook_items.append("As the ink flows")

    "Open it and see."

    "Let's add one more phrase. Try {font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}In the flow, time stands still.{/b}{/size}{/font}"
    $ notebook_items.append("In the flow, time stands still.")

    "Check it out."
    hide screen notebook_display_toggle
    
    jump ink_demo