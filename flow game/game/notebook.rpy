screen notebook_display_toggle:
    zorder 92
    imagebutton:
        idle "gui/button/notebookbutton_hover.png"
        hover "gui/button/notebookbutton_selected.png"
        action ToggleScreen("notebook_item_description")
        xalign 0.07
        yalign 0.11

    on "hide" action Hide("notebook_item_description")


default notebook_items = set()
default current_item = ""

style inv_button is frame:
    xminimum 100
    yminimum 70
    xmaximum 1100
    xpadding 50

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen notebook_item_description:
    # modal True
    window:
        background "Menu/notebook.png"
        xsize 1290
        ysize 500
        xalign 0.55
        yalign 0.4
        vbox:
            spacing 10
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 10
                xoffset 50
                yoffset 50
                style_prefix "inv"
                
                for item in get_page_items(notebook_items, current_page):
                    textbutton item:
                        action SetVariable("current_item", item)
                        selected False

            # Navigation buttons
            hbox:
                xoffset 50
                yoffset 50
                spacing 20
                if current_page > 0:
                    textbutton "Previous" action SetVariable("current_page", current_page - 1)
                if (current_page + 1) * 4 < len(notebook_items):
                    textbutton "Next" action SetVariable("current_page", current_page + 1)

label notebook_demo:   

    "Hello {font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}darling ~{/b}{/size}{/font}."

    show screen notebook_display_toggle
    "See that notebook button?"

    "Let's add a phrase to it. How about {font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}As the ink flows{/b}{/size}{/font}?"
    $ notebook_items.add("As the ink flows")

    "Open it and see."

    "Let's add one more phrase. Try {font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}In the flow, time stands still.{/b}{/size}{/font}"
    $ notebook_items.add("In the flow, time stands still.")

    "Check it out."
    hide screen notebook_display_toggle
    
    jump ink_demo

init python:
    def get_page_items(items, page, items_per_page=4):
        start = page * items_per_page
        end = start + items_per_page
        list_items = list(items)
        return list_items[start:end]

define current_page = 0

screen notebook_menu:
    modal True  # prevent it from automatically advancing or selecting options

    # lets us still click timeline button
    imagebutton:
        xalign 0.95
        yalign 0.08
        xoffset -30
        yoffset 30
        auto "gui/button/timeline_%s.png"
        action Jump ("call_timelineUI")

    window:
        background "#4f39284a"
        xsize 1290
        ysize 500
        xalign 0.5
        yalign 0.4
        vbox:
            spacing 10
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 10
                xoffset 20
                yoffset 20
                style_prefix "inv"
                
                for item in get_page_items(notebook_items, current_page):
                    if item == right_answer:
                        textbutton item:
                            action Jump (right_answer_label)
                            selected False
                    else:
                        textbutton item:
                            action Jump (wrong_answer_label)
                            selected False

            # Navigation buttons
            hbox:
                xoffset 30
                yoffset 30
                spacing 20
                if current_page > 0:
                    textbutton "Previous" action SetVariable("current_page", current_page - 1)
                if (current_page + 1) * 4 < len(notebook_items):
                    textbutton "Next" action SetVariable("current_page", current_page + 1)

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
