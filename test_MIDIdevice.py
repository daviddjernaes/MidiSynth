from unittest import TestCase
from MIDIdevice import MIDIdevice

class TestMIDIdevice(TestCase):
    midiIn = None
    midiOut = None

    def setUp(self):
        self.midi = MIDIdevice()
        self.midiIn, self.midiOut = self.midi.midiSetup()

class TestMIDIsetup(TestMIDIdevice):
    def test_midi_in(self):
        self.assertNotEqual(self.midiIn, None, msg=None)

    def test_midi_out(self):
        self.assertNotEqual(self.midiOut, None, msg=None)

class TestGetStartNote(TestMIDIdevice):
    def test_start_note_not_none(self):
        print("Press key to map sample to: ")
        startNote = self.midi.getStartNote(self.midiIn, self.midiOut)
        self.assertNotEqual(None, startNote, msg=None)
