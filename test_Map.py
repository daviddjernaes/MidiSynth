from unittest import TestCase
from Map import Map
import pyrubberband as prb
import numpy as np
from scipy.io.wavfile import write, read

class TestMap(TestCase):
    def setUp(self):
        self.keymap = Map(69, None, 44100)

class TestInit(TestMap):
    def test_startNote_initializes_properly(self):
        self.assertEqual(self.keymap.startNote, 69)

    def test_sample_initializes_properly(self):
        self.assertEqual(self.keymap.sample, None)

    def test_SampleRate_initializes_properly(self):
        self.assertEqual(self.keymap.rate, 44100)

class TestStartFreq(TestMap):
    def test_StartFreq_calculation(self):
        self.assertEqual(self.keymap.startFreq, 440)

