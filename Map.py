import pyrubberband as prb
import numpy as np

class Map():
    sample = None
    sampRate = None
    startNote = None
    startFreq = None
    midiA440 = 69
    midiLow = 21
    midiHigh = 108

    def __init__(self, startNote, sample, rate):
        self.sample = sample
        self.rate = rate
        self.startNote = startNote
        self.startFreq = Map.setStartFreq(self, self.startNote)

    #no current use for this function...saving in case it comes into play later
    def setStartFreq(self, startNote):
        #difference between input note and A440, which maps to 69 on a MIDI keyboard
        noteDiff = startNote - self.midiA440
        startFreq = 440 * (2**(noteDiff / 12))

        #sanity check
        #print("The starting frequency is: ", startFreq)

        return startFreq

    #pyrubberband requires sample to be of type float32 np.ndarray
    #pygame.mixer requires int16 np.ndarray
    def pitchshift(self, n):
        note = n - self.startNote
        sound = np.int16(prb.pitch_shift(self.sample, self.rate, note) * (2 ** 15))

        return sound
