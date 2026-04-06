import sys
from psychopy import logging
logging.console.setLevel(logging.DEBUG)
from psychopy import prefs #must be set before importing sound
prefs.hardware['audioLib'] = ['pygame'] #must be set before importing sound
from psychopy import sound, core

print('using pygame to test audio')

highA = sound.Sound('A', octave=3, sampleRate=44100, secs=0.8, stereo=True)
highA.setVolume(0.8)
tick = sound.Sound(800, secs=0.01, sampleRate=44100, stereo=True)
tock = sound.Sound('600', secs=0.01, sampleRate=44100, stereo=True)

highA.play()
core.wait(0.8)
tick.play()
core.wait(0.4)
tock.play()
core.wait(0.6)

if sys.platform == 'darwin':
    ding = sound.Sound('sounds/ding.wav')
    ding.play()
    
    core.wait(1.0)
    
    tada = sound.Sound('tada.wav')
    tada.play()
    
    core.wait(2)
print('done')

core.quit()