#Music from https://downloads.khinsider.com/game-soundtracks/album/pokemon-gameboy-sound-collection
# and http://www.pokezorworld.com/anime/poke/sounds.shtml
from pygame import mixer

mixer.init()

mixer.music.set_volume(0.2)
classic_intro = mixer.Sound("music/classic_intro.wav")
mixer.music.load("music/classic_intro.wav")
mixer.music.play(-1)
