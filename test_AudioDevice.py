from unittest import TestCase
from AudioDevice import AudioDevice
import numpy as np
from scipy.io.wavfile import write, read

class TestAudioDevice(TestCase):
    def setUp(self):
        self.audio = AudioDevice()

class TestRecord(TestAudioDevice):
    def test_record_does_not_clip_signal(self):
        testRec = self.audio.record()
        self.assertLess(np.max(np.abs(testRec)), 1)

