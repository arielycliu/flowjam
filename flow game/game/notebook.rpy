screen notebook_display_toggle:
    zorder 92
    imagebutton:
        idle "gui/button/notebookbutton_hover.png"
        hover "gui/button/notebookbutton_selected.png"
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


label notebook_demo:   

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

screen notebook_menu:      
    modal True  
    window:
        background "#4f39284a"
        xsize 1290
        ysize 500
        xalign 0.5
        yalign 0.4
        vbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in notebook_items:
                if item == right_answer:
                    textbutton item:
                        action Jump (right_answer_label)
                        selected False
                else:
                    textbutton item:
                        action Jump (wrong_answer_label)
                        selected False

# label notebook_menu_demo:
#     define wrong_answer_label = "label_b"
#     define right_answer_label = "label_a"
#     define right_answer = "a"
#     show screen notebook_display_toggle
#     show screen notebook_menu
#     "What will you choose?"

# label label_a:
#     hide screen notebook_menu
#     $ notebook_items.remove("a")
#     "You have a"
#     return

# label label_b:
#     hide screen notebook_menu
#     $ notebook_items.remove("b")
#     "You have b, which is wrong"
#     return
