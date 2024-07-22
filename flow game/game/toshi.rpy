define toshi = Character("Toshi")
define toshi_unknown = Character("???")

screen fullscreen_garden:
    add "images/Backgrounds/bg garden.jpg" xpos 0 ypos 0 size (config.screen_width, config.screen_height) 

transform stretch_to_fill:
    xysize (config.screen_width, config.screen_height)

label toshi1:
    hide screen black_screen
    $ part1 = 1
    scene
    $ toshi_bookmark = "toshi1"
    show screen basics
    show bg garden
    "On a balcony overlooking a grand maple garden, a mortal sits, surrounded by balls of paper."

    show toshi sadmasked
    toshi_unknown "This is hopeless..."

    toshi_unknown "..."

    show toshi frownmasked
    toshi_unknown "I'm hopeless..."

label toshi11:
    scene
    $ toshi_bookmark = "toshi11"
    show screen basics
    show bg garden

    show toshi frownmasked
    "Suddenly, he straightens."

    show toshi surprisedmasked
    "His mask swivels toward me. He spots me and springs up, slipping into a smile with fox-like fluidity."

label toshi12:
    scene
    $ toshi_bookmark = "toshi12"
    show screen basics
    show bg garden

    show toshi surprisedmasked
    toshi_unknown "Oh!"

    toshi_unknown "My prayers answered."

    show toshi smilemasked
    toshi_unknown "Perhaps I was right to branch out."

    toshi_unknown "The local gods never hear."

label toshi13:
    scene
    $ toshi_bookmark = "toshi13"
    show screen basics
    show bg garden

    show toshi smile
    toshi "Pleased to meet you."
    
    toshi "And shocked. I wasn't sure you were real."

    show toshi smile
    mc "I do try my best to be."

    show toshi grin
    toshi "I don't doubt it."

label toshi14:
    scene
    $ toshi_bookmark = "toshi14"
    show screen basics
    show bg garden

    show toshi smile
    toshi "My name's Toshi."

    show toshi grin
    toshi "Did you know that already?"

    toshi "You certainly look like you did."

    mc "I did. I can read it in your eyes, you know. Eyes will whisper your name to others, if you're not careful."

label toshi15:
    scene
    $ toshi_bookmark = "toshi15"
    show screen basics
    show bg garden

    show toshi satisfied
    toshi "Naturally. That makes sense."
    
    show toshi smile
    toshi "I'll have to remember that."

    show toshi grin
    toshi "Thank you for coming."

label toshi16:
    scene
    $ toshi_bookmark = "toshi16"
    show screen basics
    show bg garden

    show toshi sad
    toshi "I..."

    show toshi grin
    toshi "I admit, I've been struggling."

    show toshi smile
    toshi "I'm trying to put a poem together."

label toshi17:
    scene
    $ toshi_bookmark = "toshi17"
    show screen basics
    show bg garden

    show toshi smile
    toshi "There's this girl..."

    mc "Ah. A classic motivator for writing, if there ever was one."

    show toshi grin
    toshi "You understand, then."

    show toshi smile
    toshi "It's quite a task."

label toshi18:
    scene
    $ toshi_bookmark = "toshi18"
    show screen basics
    show bg garden

    show toshi frown
    toshi "I can never express what I want to say."

    toshi "And not something trite."

    show toshi bored
    toshi "Not like..."

    show toshi smilemasked
    $ notebook_items.add("Her ocean-blue eyes and snow-white hair captured my attention. When she smiled, she was the only person in the room to me.")
    toshi "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}Her ocean-blue eyes and snow-white hair captured my attention. When she smiled, she was the only person in the room to me.{/b}{/size}{/font}"

label toshi19:
    scene
    $ toshi_bookmark = "toshi19"
    show screen basics
    show bg garden

    show toshi sad
    toshi "Not like that."

    show toshi smile
    toshi "Although it's true."

    toshi "I don't know what to say."

    show toshi grin
    toshi "I've never wooed anyone."

label toshi1_menu:
    scene
    $ toshi_bookmark = "toshi1_menu"
    show screen basics
    show bg garden

    show toshi bored
    toshi "Honestly, I'm not sure I even should."
    $ wrong_answer_label = "toshi1_wrong"
    $ right_answer_label = "toshi1_right"
    $ right_answer = "People can feel when you're being genuine, even if they think they can't tell."
    show screen notebook_menu
    "What should I say?"

label toshi1_wrong: 
    $ ink = ink - 5
    show toshi frownmasked
    toshi "What does that mean?"
    jump toshi1_menu

label toshi1_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ notebook_items.remove("People can feel when you're being genuine, even if they think they can't tell.")
    show toshi sad
    toshi "Huh?"
    jump toshi2

label toshi2:
    $ part1 = 2

    scene
    $ toshi_bookmark = "toshi2"
    show screen basics
    show bg garden

    show toshi smile
    toshi "You hear that a lot, right?"

    show toshi smile
    toshi "But being myself is a bit difficult."

    show toshi grin
    toshi "I've worn a few too many faces to do that."

label toshi21:
    scene
    $ toshi_bookmark = "toshi21"
    show screen basics
    show bg garden

    show toshi grin
    toshi "It's hard to be sure a certain face is me."

    mc "Faces...?"

    mc "At any rate, it's sound advice."

    "Or at least, I think so. I've never been in love."

label toshi22:
    scene
    $ toshi_bookmark = "toshi22"
    show screen basics
    show bg garden

    show toshi sad
    mc "If you're truly meant for each other, I'm sure none of your faces will scare her away."

    show toshi smilemasked
    toshi "I suppose that's what they say."

    show toshi smile
    toshi "I guess it's nice to hear that."

label toshi23:
    scene
    $ toshi_bookmark = "toshi23"
    show screen basics
    show bg garden

    show toshi sad
    toshi "I've never really chosen to be myself."

    $ notebook_items.add("I've only kept the pieces that are inoffensive to everyone.")
    toshi "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}I've only kept the pieces that are inoffensive to everyone.{/b}{/size}{/font}"

    show toshi grin
    $ notebook_items.add("A handsome smile and a flattering voice will get you far.")
    toshi "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}A handsome smile and a flattering voice will get you far.{/b}{/size}{/font}"

label toshi24:
    scene
    $ toshi_bookmark = "toshi24"
    show screen basics
    show bg garden

    show toshi sad
    toshi "I don't think I could keep that face up forever."

    show toshi sad
    toshi "It tires me out."

label toshi25:
    scene
    $ toshi_bookmark = "toshi25"
    show screen basics
    show bg garden

    show toshi smile
    toshi "So really, I've never been very open with her."

    show toshi sad
    toshi "I'm used to having secrets. Not as used to having a friend."

label toshi26:
    scene
    $ toshi_bookmark = "toshi26"
    show screen basics
    show bg garden

    show toshi sad
    mc "Well, I'm certainly no god of romance, but..."
    
    mc "I don't see how you expect to be close with her if you won't let her into your life."

    show toshi bored
    toshi "Perhaps."

label toshi27:
    scene
    $ toshi_bookmark = "toshi27"
    show screen basics
    show bg garden

    show toshi sad
    $ notebook_items.add("But honesty never ends well in the long run. I know that from experience.")
    toshi "{font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}But honesty never ends well in the long run. I know that from experience.{/b}{/size}{/font}"

    show toshi sadmasked
    toshi "I'm never letting that happen again."

label toshi2_menu:
    scene
    $ toshi_bookmark = "toshi2_menu"
    show screen basics
    show bg garden

    show toshi frownmasked
    toshi "Maybe this really is a bad idea."
    $ wrong_answer_label = "toshi2_wrong"
    $ right_answer_label = "toshi2_right"
    $ right_answer = "But if I keep pretending, I'm only going to be living someone else's life for the rest of mine."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What should I say?"

label toshi2_wrong: 
    $ ink = ink - 5
    show toshi frownmasked
    toshi "What does that mean?"
    jump toshi2_menu

label toshi2_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ notebook_items.remove("But if I keep pretending, I'm only going to be living someone else's life for the rest of mine.")
    show toshi grin
    toshi "Ah, you make such a good case."
    jump toshi3

label toshi3:
    $ part1 = 3
    scene
    $ toshi_bookmark = "toshi3"
    show screen basics
    show bg garden

    show toshi smile
    toshi "As though it is so simple."

    show toshi smile
    toshi "Write what you feel."

    show toshi sad
    toshi "To share your thoughts is to give others power over you."

    toshi "It costs you to be honest."

label toshi31:
    scene
    $ toshi_bookmark = "toshi31"
    show screen basics
    show bg garden

    show toshi grin
    toshi "Maybe I'm a coward, but I think if she knew how I felt..."

    show toshi sad
    toshi "It would scare her."

    show toshi smile
    toshi "I don't think I'm an easy person to love."

    show toshi bored
    toshi "Really, keeping some distance is better for everyone."

label toshi32:
    scene
    $ toshi_bookmark = "toshi32"
    show screen basics
    show bg garden

    show toshi grin
    $ notebook_items.add("lying can always solve problems. Or make things better. Or if not better, more interesting.")
    toshi "That's why I find {font=gui/font/1546 poliphile w00 normal.ttf}{size=24}{b}lying can always solve problems. Or make things better. Or if not better, more interesting.{/b}{/size}{/font}"

    toshi "Or if not more interesting..."

    toshi "Easier."

label toshi33:
    scene
    $ toshi_bookmark = "toshi33"
    show screen basics
    show bg garden

    show toshi smile
    toshi "I don't know if love is a good enough reason to change that."

    toshi "No matter how special she may be."

    show toshi grin
    toshi "No matter how many rooms she lights up."

    toshi "Maybe we can remain friends..."

    show toshi sadmasked
    toshi "Forever."

label toshi3_menu:
    scene
    $ toshi_bookmark = "toshi3_menu"
    show screen basics
    show bg garden

    show toshi frownmasked
    toshi "Maybe this really is a bad idea."
    $ wrong_answer_label = "toshi3_wrong"
    $ right_answer_label = "toshi3_right"
    $ right_answer = "at least I will go to my own death knowing that I have not let my dreams slip idly by."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What should I say?"

label toshi3_wrong: 
    $ ink = ink - 5
    show toshi frownmasked
    toshi "What does that mean?"
    jump toshi3_menu

label toshi3_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    $ notebook_items.remove("at least I will go to my own death knowing that I have not let my dreams slip idly by.")
    show toshi sad
    toshi "That's..."
    jump toshi31

label toshi31:
    $ part1 = 4
    scene
    $ toshi_bookmark = "toshi31"
    show screen basics
    show bg garden

    show toshi smile
    toshi "I don't know."

    toshi "I don't know how to feel. I'll have to think on it."

    show toshi grin
    toshi "Please leave me alone for a while."

label toshi4:
    $ part1 = 4
    scene
    $ toshi_bookmark = "toshi4"
    show screen basics
    show bg garden

    # so that from now on, every time you jump back to Toshi, he's writing
    while True:
        show toshi smile
        "Toshi thumbs the edges of his mask, and flinches when he pokes the ears too hard."
        show toshi frown
        "Toshi thinks about his words. He carefully makes a mark on the paper, as though it will run away if he's not careful."
        show toshi grin
        "Toshi bursts out laughing to himself for no apparent reason at all."
