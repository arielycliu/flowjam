transform default_zoom:
    zoom 1.5
image elias happy:
    "images/Elias/elias happy.png"
    default_zoom
image elias neutral:
    "images/Elias/elias neutral.png"
    default_zoom
image elias smile:
    "images/Elias/elias smile.png"
    default_zoom
image elias surprise:
    "images/Elias/elias surprise.png"
    default_zoom

image synthea angry:
    "images/Synthea/synthea angry.png"
    default_zoom
image synthea grin:
    "images/Synthea/synthea grin.png"
    default_zoom
image synthea happy:
    "images/Synthea/synthea happy.png"
    default_zoom
image synthea sad:
    "images/Synthea/synthea sad.png"
    default_zoom
image synthea shocked:
    "images/Synthea/synthea shocked.png"
    default_zoom

image peregrine confused:
    "images/Peregrine/peregrine confused.png"
    default_zoom
image peregrine distracted:
    "images/Peregrine/peregrine distracted.png"
    default_zoom
image peregrine mad:
    "images/Peregrine/peregrine mad.png"
    default_zoom
image peregrine neutral:
    "images/Peregrine/peregrine neutral.png"
    default_zoom
image peregrine shocked:
    "images/Peregrine/peregrine shocked.png"
    default_zoom
image peregrine smile:
    "images/Peregrine/peregrine smile.png"
    default_zoom
image peregrine talking:
    "images/Peregrine/peregrine talking.png"
    default_zoom
image peregrine tired:
    "images/Peregrine/peregrine tired.png"
    default_zoom

image nostro angry:
    "images/Nostro/nostro angry.png"
    default_zoom
image nostro happy:
    "images/Nostro/nostro happy.png"
    default_zoom
image nostro knowing:
    "images/Nostro/nostro knowing.png"
    default_zoom
image nostro sign:
    "images/Nostro/nostro sign.png"
    default_zoom
image nostro smile:
    "images/Nostro/nostro smile.png"
    default_zoom
image nostro veryhappy:
    "images/Nostro/nostro veryhappy.png"
    default_zoom
image nostro worried:
    "images/Nostro/nostro worried.png"
    default_zoom

image toshi angry:
    "images/Toshi/toshi angry.png"
    default_zoom
image toshi bored:
    "images/Toshi/toshi bored.png"
    default_zoom
image toshi frown:
    "images/Toshi/toshi frown.png"
    default_zoom
image toshi frownmasked:
    "images/Toshi/toshi frownmasked.png"
    default_zoom
image toshi grin:
    "images/Toshi/toshi grin.png"
    default_zoom
image toshi happy:
    "images/Toshi/toshi happy.png"
    default_zoom
image toshi sad:
    "images/Toshi/toshi sad.png"
    default_zoom
image toshi sadmasked:
    "images/Toshi/toshi sadmasked.png"
    default_zoom
image toshi satisfied:
    "images/Toshi/toshi satisfied.png"
    default_zoom
image toshi smile:
    "images/Toshi/toshi smile.png"
    default_zoom
image toshi smilemasked:
    "images/Toshi/toshi smilemasked.png"
    default_zoom
image toshi suprisedmasked:
    "images/Toshi/toshi suprisedmasked.png"
    default_zoom

define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

label start:
    play music gamemusic

    jump tutorial

label game_end:
    "Tada! You have won the game"
    return