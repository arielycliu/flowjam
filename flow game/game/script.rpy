transform default_character_zoom:
    zoom 1.3
    ypos 0.9
    xpos 0.5
image elias happy:
    "images/Elias/elias happy.png"
    default_character_zoom
image elias neutral:
    "images/Elias/elias neutral.png"
    default_character_zoom
image elias smile:
    "images/Elias/elias smile.png"
    default_character_zoom
image elias surprise:
    "images/Elias/elias surprise.png"
    default_character_zoom

image synthea angry:
    "images/Synthea/synthea angry.png"
    default_character_zoom
image synthea grin:
    "images/Synthea/synthea grin.png"
    default_character_zoom
image synthea happy:
    "images/Synthea/synthea happy.png"
    default_character_zoom
image synthea sad:
    "images/Synthea/synthea sad.png"
    default_character_zoom
image synthea shocked:
    "images/Synthea/synthea shocked.png"
    default_character_zoom

image peregrine confused:
    "images/Peregrine/peregrine confused.png"
    default_character_zoom
image peregrine distracted:
    "images/Peregrine/peregrine distracted.png"
    default_character_zoom
image peregrine mad:
    "images/Peregrine/peregrine mad.png"
    default_character_zoom
image peregrine neutral:
    "images/Peregrine/peregrine neutral.png"
    default_character_zoom
image peregrine shocked:
    "images/Peregrine/peregrine shocked.png"
    default_character_zoom
image peregrine smile:
    "images/Peregrine/peregrine smile.png"
    default_character_zoom
image peregrine talking:
    "images/Peregrine/peregrine talking.png"
    default_character_zoom
image peregrine tired:
    "images/Peregrine/peregrine tired.png"
    default_character_zoom

image nostro angry:
    "images/Nostro/nostro angry.png"
    default_character_zoom
image nostro happy:
    "images/Nostro/nostro happy.png"
    default_character_zoom
image nostro knowing:
    "images/Nostro/nostro knowing.png"
    default_character_zoom
image nostro neutral:
    "images/Nostro/nostro neutral.png"
    default_character_zoom
image nostro sigh:
    "images/Nostro/nostro sigh.png"
    default_character_zoom
image nostro smile:
    "images/Nostro/nostro smile.png"
    default_character_zoom
image nostro veryhappy:
    "images/Nostro/nostro veryhappy.png"
    default_character_zoom
image nostro worried:
    "images/Nostro/nostro worried.png"
    default_character_zoom

image toshi angry:
    "images/Toshi/toshi angry.png"
    default_character_zoom
image toshi bored:
    "images/Toshi/toshi bored.png"
    default_character_zoom
image toshi frown:
    "images/Toshi/toshi frown.png"
    default_character_zoom
image toshi frownmasked:
    "images/Toshi/toshi frownmasked.png"
    default_character_zoom
image toshi grin:
    "images/Toshi/toshi grin.png"
    default_character_zoom
image toshi happy:
    "images/Toshi/toshi happy.png"
    default_character_zoom
image toshi sad:
    "images/Toshi/toshi sad.png"
    default_character_zoom
image toshi sadmasked:
    "images/Toshi/toshi sadmasked.png"
    default_character_zoom
image toshi satisfied:
    "images/Toshi/toshi satisfied.png"
    default_character_zoom
image toshi smile:
    "images/Toshi/toshi smile.png"
    default_character_zoom
image toshi smilemasked:
    "images/Toshi/toshi smilemasked.png"
    default_character_zoom
image toshi surprisedmasked:
    "images/Toshi/toshi surprisedmasked.png"
    default_character_zoom

transform stretch_to_fill:
    xysize (config.screen_width, config.screen_height)
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
image bg pinkgalaxy:
    "images/Backgrounds/bg pinkgalaxy.jpg"
    stretch_to_fill
image bg garden:
    "images/Backgrounds/bg garden.jpg"
    stretch_to_fill
image bg knightroom:
    "images/Backgrounds/bg peasanthouse.jpg"
    xysize (config.screen_width, config.screen_height + 200)
    ypos 1.1
image bg castle:
    "images/Backgrounds/bg bookshop.jpg"
    xpos 0.45
    xysize (config.screen_width + 199, config.screen_height)
image bg office:
    "images/Backgrounds/bg futureoffice.jpg"
    stretch_to_fill
image bg breakroom:
    "images/Backgrounds/bg futureroom.jpg"
    stretch_to_fill

define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

default name = "???"
default ink = 100

screen basics:
    use inkbar
    use notebook_display_toggle
    use timelineButton
    use monitor_ink

label start:
    play music gamemusic

    $ toshi_bookmark = "toshi1"
    $ peregrine_bookmark = "peregrine1"
    $ nostro_bookmark = "nostro1"
    $ synthea_bookmark = "synthea1"

    $ part1 = 0
    $ part2 = 0
    $ part3 = 0
    $ part4 = 0

    jump tutorial

init python:
    def check_ink():
        if ink <= 0:
            renpy.jump("game_over")

label game_over:
    "Unfortunately, you have run out of ink..."
    return

label game_end:
    "Tada! You have won the game"
    return