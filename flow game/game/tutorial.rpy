define elias = Character("Elias", color="#84622e")
define mc = Character("???", color="#685d4b")

screen black_screen:
    frame:
        background "#000000"

label tutorial:
    $ ink = 100

    scene bg pinkgalaxy

    "But am I truly ready?"

    elias "I see you have arrived."

    show elias happy
    elias "You look nervous."

    "I... am."

    show elias neutral
    elias "There is no need to be. Trust in your knowledge. We have taught you all that we know."

    show elias smile
    elias "And now, they shall have their god. You, the creator of stories - the soul of the written word - the inksmith."

    show elias neutral
    elias "But what shall your followers call you? You shall need a title, after all."

    python:
        name = renpy.input("What do your followers call you?")
        name = name.strip() or "Inksmith"

    define mc = Character("[name]", color="#685d4b")
    
    show elias smile
    elias "Very well then. You are to be [name]. The name suits you."

    show elias neutral
    elias "Time constrains them, [name]. Not us."

    elias "You may travel between moments as you like, should the occasion demand it."

    show elias smile
    show screen timelineButton
    elias "Take a look at the timeline map."

    show elias neutral
    elias "Each section represents the timeline of one of your subjects."

    show elias smile
    elias "Time flows steadily on, but we have already taught you to swim."

    elias "You'll be able to weave between different time periods as you wish. But the progress you make in each period cannot be undone."

    show elias neutral
    elias "A mere mortal cannot comprehend time like we do, such precautions are necessary."

    show elias smile
    show screen notebook_display_toggle
    elias "Let me show you your second tool, the notebook."

    show elias neutral
    elias "Words, like ink, flow and seep into the fabric of time."

    show elias smile
    elias "As the goddess of words and ink, I have no doubt that your ink will always be flowing across the pages of this notebook."

    show elias neutral
    elias "And when the time comes, and they beg you to guide them. With a notebook full of phrases, you will anyways have the right words to say."

    elias "But choose wisely, for each word can only be written once, and their echoes will shape destiny."
    
    show elias smile
    elias "You are {font=gui/font/1546 Poliphile W00 Normal.ttf}{size=24}{b}ready{/b}{/size}{/font} for your first phrase."
    $ notebook_items.add("ready")

    elias "Open the notebook"

    elias "Now remember, your power comes only from your followers, and as a fledgling god, you have them in short supply."

    elias "Do not waste ink recklessly. Every word of advice will cost you."

    show screen inkbar
    $ ink = 0
    while ink < 100:
        $ ink += 1
        pause(0.0001)
    $ ink = 100
    elias "When you are out of ink, you are out of words. And you cannot be a goddess of words, without any words."

    show elias happy
    elias "Should you prove yourself worthy, and cement yourself in the hearts of your devoted, you you will enter into the pantheon."
    
    show elias neutral
    elias "I have great faith in you, [name]."

    $ narrator("Are you ready?", interact=False)
    $ result = renpy.display_menu([ (item, "Good") for item in notebook_items ])
    $ notebook_items.remove("ready")

    show elias smile
    elias "Good"

    hide elias smile

    "I feel a dam breaking."

    "A cacophany of voices spills into my mind - [name] {i}[name]{/i} [name!u] [name] [name]"

    "My followers. The beings under my care."

    "Seizing upon one at random, I close my eyes and let time's current sweep me away."

    $ part1 = 1
    $ part2 = 1
    $ part3 = 1
    $ part4 = 1

    show screen black_screen with dissolve

    jump toshi1