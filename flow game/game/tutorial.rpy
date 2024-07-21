label tutorial:
    $ ink = 100

    scene bg skies
    stop music fadeout 1.0
    play music "tutorial.mp3" fadein 1.0

    "But am I truly ready?"

    elias "I see you have arrived."

    elias "You look nervous."

    mc "I... am."

    elias "There is no need to be. Trust in your knowledge. We have taught you all that we know."

    elias "And now, they shall have their god. You, the creator of stories - the soul of the written word - the inksmith."

    elias "But what shall your followers call you? You shall need a title, after all."

    python:
        name = renpy.input("What do your followers call you?")
        name = name.strip() or "Inksmith"

    define mc = Character("[name]", color="#685d4b")
    
    show elias smile
    elias "Very well then. You are to be <name>. The name suits you."

    show elias neutral
    elias "Time constrains them, [name]. Not us."

    elias "You may travel between moments as you like, should the occasion demand it."

    show elias smile
    elias "Simply think of it as {ink}saving{/ink} a bookmark for a later time, if you will."

    elias "Go on now. Give it a try."

    """
    T
    You are ready. Should you prove yourself worthy, and cement yourself in the hearts of your devoted, you you will enter into the pantheon.

    I have great faith in you, name.


    I shall leave you with one last teaching: the world of mortals 

    I shall leave you with one last yeaching, then.

    The world of mortals is constrained by the bounds of time, but we are not.



    The world of mrotals is constrained by time. It marches onward, relentless, and always in the same everlasting line.

    But gods such as us do not live that way.

    We exist instead in the moments - the  times of need, where a prayer is made in our name.

    As such, it may be wise to create points which you can return to, should you wish. 



    above bookmark quote

    try it now mechanic

    Perfect. 


    Remember: should you wish to save the spirit of inspiration



    ok how about you say the first bit

    a What was all that training for if you are going to teach name the important bits now?

    elias oh, eliza. one day, you will understand. sometimes, the best things are simply to be saved for last/






    Your ink lends you the power to save words of your followers for inspiration. Any of them.

    But do not squander it; your power comes only from your followers, and as a fledgling god, you have them in short supply.

    Spend your energy wisely, and you may attract more yet.

    Go on, then. I wish you all the best.
    """

    show elias happy
    elias "Goodbye, [name]!"


    "As they wave, I feel a dam breaking."

    "A cacophany of voices spills into my mind - [name] {i}[name]{/i} [name!u] [name] [name]"

    "My followers. The beings under my care."

    "Seizing upon one at random, I close my eyes and let time's current sweep me away."

    jump toshi