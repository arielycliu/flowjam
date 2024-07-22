define synthea = Character("Synthea")
label synthea1:
    $ part4 = 1
    scene bg office at stretch_to_fill zorder 0

    "A mortal is tapping away at a shimmering image of a keyboard in a technology-filled office."

    "Ah, the holographic age - the site of the death of the handwritten word."

    "The buzz of writing activity energizes me, though, and I glance at the mortal's screen."

    "Bright symbols I just barely recognize flash across it at breakneck speed. It appears to be some sort of adapted version of shorthand."

    "The mortal takes a sip from her flask, then spots me."

    show synthea shocked
    synthea "!"

    "She makes a zipping motion across her mouth, then turns off her screen and walks slowly over to the break room."

    "Wordlessly, I follow."

    scene bg breakroom
    "Once inside, she closes the door and gives me a big smile."

    show synthea happy
    synthea "Hello, [name]!"

    synthea "It looks like my interest in ancient mythology paid off."

    synthea "Don't worry, I won't tell anyone we met."

    "Bafflingly, she grabs my hand and shakes it with enthusiasm."

    show synthea grin
    synthea "It's nice to meet you!"

    mc "You're... very earnest."

    show synthea happy
    synthea "Yes!"

    synthea "It pays to be genuine in sales nowadays."

    synthea "{ink}People can feel when you're being genuine, even if they think they can't tell.{/ink}"

    synthea "And I write ad copy for a living."

    synthea "With so much going on in the world - automated false human identity replacements, eyescanner scams - people just want to believe they can trust you."

    synthea "What I'm not as good at is hooking people in."

    synthea "Getting their attention - now, that's a tougher sell."

    synthea "That's exactly why I need your advice."

    synthea "I'm working on marketing a lot of things right now."

    synthea "Why, if I listed them all, we'd be here all day!"

    synthea "So I'm not sure I'm looking for any specific advice here."


label synthea1_menu:
    show synthea grin
    synthea "Any thoughts?"
    define wrong_answer_label = "synthea1_wrong"
    define right_answer_label = "synthea1_right"
    define right_answer = "Ah, well. Times are changing. That is inevitable. We can only hope to change them for the better."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label synthea1_wrong: 
    $ ink = ink - 5
    synthea "That wasn't what I really had in mind..."
    jump synthea1_menu

label synthea1_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    synthea "Hmm. There's a thought, huh?"

    jump synthea2

    # MENU - Sometimes, I find the unexpected to be the most pleasing.


label synthea2:
    $ part4 = 2
    synthea "You may just be right."

    synthea "That'll work really great for the strobe light tanning bed!"

    show synthea happy
    synthea "I think I just lack inspiration, lately."

    synthea "I believe in our clients' projects. I really do. And I want them to succeed."

    synthea "{ink}You already know you've got the best product in town. You just need your buyers to believe that.{/ink} But that's precisely the problem."

    synthea "Sometimes, customers just don't care about quality."
    
    synthea "All they want is something they feel good about purchasing!"
    
    synthea "Appealing to emotions, right?"

    show synthea shocked
    synthea "But there's just so many things people don't care about anymore."

    synthea "Climate change, animal protection, addiction, - they're worn out on caring."

    synthea "I suppose all the advertising hasn't really helped."

    show synthea happy
    synthea "At this point, I'm not sure what kind of messaging will even engage people."

    synthea "But if there's nothing to write about, then there's nothing to set your products apart!"


label synthea2_menu:
    synthea "The 2-in-1 baby swing and stand mixer isn't going to sell itself."
    define wrong_answer_label = "synthea2_wrong"
    define right_answer_label = "synthea2_right"
    define right_answer = "We have to believe that things can get better."
    show screen notebook_display_toggle
    show screen notebook_menu
    "What will you choose?"

label synthea2_wrong: 
    $ ink = ink - 5
    synthea "What are you saying?"
    jump synthea2_menu

label synthea2_right: 
    hide screen notebook_menu
    $ ink = ink - 5
    show synthea shocked
    synthea "That's... true."
    jump synthea3

label synthea3:
    $ part4 = 3
    synthea "Maybe hope is what's missing in this world."

    show synthea sad
    synthea "I... don't think I like my job much anymore, to be honest."

    synthea "{ink}We've been working so hard to make things appealing to everyone, we haven't stopped to wonder if we should.{/ink}"