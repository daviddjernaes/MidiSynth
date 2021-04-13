# MIDIdevice.py
from __future__ import print_function
import logging
import sys
from rtmidi.midiutil import open_midiinput, open_midioutput
from pygame import mixer, sndarray

class MIDIdevice:
    def midiSetup(self):
        #debug
        #log = logging.getLogger('midiin_poll')
        #logging.basicConfig(level=logging.DEBUG)

        # Prompts user for MIDI input port, unless a valid port number or name
        # is given as the first argument on the command line.
        # API backend defaults to ALSA on Linux.
        # print("input value: ")
        port = sys.argv[1] if len(sys.argv) > 1 else None

        try:
            midiin, port_name = open_midiinput(port)
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        try:
            midiout, port_name = open_midioutput(port)
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        return midiin, midiout

    def getStartNote(self, midiin, midiout):
        message = [0]
        received = False

        while not received:
            temp = message[0]  #keeps message variable in scope
            msg = midiin.get_message()
            if msg:
                message, deltatime = msg
                midiout.send_message(message)
                received = True

        startNote = message[1]

        #make sure we don't have a residual note-on message
        message[0] = 128
        midiout.send_message(message)

        return startNote

    def playSound(self, midiin, midiout, midiMap, audio):
        print("\nLoading sample to MIDI device...")

        #map samples to MIDI notes
        #the following is adapted from https://github.com/Zulko/pianoputer/blob/master/pianoputer.py
        kybdRange = range(21, 109)
        pitchShftdSmpls = [midiMap.pitchshift(n) for n in kybdRange]
        mixer.init(48000, -16, 1, 2048)

        keys = kybdRange
        sounds = map(sndarray.make_sound, pitchShftdSmpls)  #***does this appropriately make a sound object?
        keySound = dict(zip(keys, sounds))
        isPlaying = {k: False for k in keys}

        print("\nReady for midi controller input. Press Control-C to exit.")

        try:
            while True:
                msg = midiin.get_message()
                if msg:
                    message, deltatime = msg
                    key = message[1]

                    #if key is pressed
                    if message[0] == 144:
                        if(key in keySound.keys()) and (not isPlaying[key]):
                            keySound[key].play()
                            isPlaying[key] = True

                    #if key is released
                    elif message[0] == 128 and key in keySound.keys():
                        keySound[key].fadeout(50)
                        isPlaying[key] = False

        except KeyboardInterrupt:
            print('')
        finally:
            print("Exit.")
            midiin.close_port()
            midiout.close_port()
            del midiin
            del midiout

