from unittest import TestCase
from SampLib import sampLib

class TestSampLib(TestCase):
    def setUp(self):
        self.library = sampLib()

class TestInit(TestSampLib):
    def test_library_size_inits_to_greaterOrEqToZero(self):
        self.assertGreaterEqual(self.library.lib.size, 0)

class TestAddSample(TestSampLib):
    def test_addSample_adds_one_to_library(self):
        numSamps = self.library.lib.size
        self.library.addSample("test")
        self.assertEqual(self.library.lib.size, numSamps + 1)

    def test_addSample_names_correctly(self):
        self.library.addSample("test")
        i = self.library.lib.size
        self.assertEqual(self.library.lib[i-1], "test.wav")

class TestDelSample(TestSampLib):
    def test_delSample_subtracts_one_from_library(self):
        numSamps = self.library.lib.size
        if numSamps > 0:
            self.library.delSample(0)
            self.assertLessEqual(self.library.lib.size, numSamps - 1)
        else:
            self.assertEqual(self.library.lib.size, 0)
