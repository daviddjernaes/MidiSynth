import sounddevice as sd
from scipy.io.wavfile import write, read
import time
import numpy as np
import librosa
import os

class AudioDevice:
    sampleRate = 48000
    channels = 1

    def record(self):
        '''
        def trimSamp(sample):
            samp = np.array(sample.astype(np.float32))
            scaledSamp = samp * (2 ** -15)

            #remove silence at the beginning and end of the sample
            trimmedSamp, _ = librosa.effects.trim(scaledSamp, 60)

            print("Sample: ", librosa.get_duration(scaledSamp))
            print("Trimmed Sample: ", librosa.get_duration(trimmedSamp))

            # rescale to int16
            rescaledSamp = trimmedSamp * (2 ** 15)
            finalSamp = np.array(rescaledSamp.astype(np.int16))

            return finalSamp
        '''

        def countdown(sec):
            while(sec > 0):
                print(sec, end = '\n')
                time.sleep(1)
                sec -= 1

        countdown(3)

        duration = 2
        audioSamp = sd.rec(int(duration * self.sampleRate), dtype = 'int16',
                           samplerate = self.sampleRate, channels = self.channels)
        print('\n***Recording***')
        sd.wait()

        #normalize the sample
        #samp = AudioDevice.trimSamp(self, audioSamp)
        samp = audioSamp
        finalSamp = samp / (np.max(np.abs(samp), axis = 0) / 0.95)

        return finalSamp

    def play(self, sample):
        sd.play(sample, self.sampleRate)

    def save(self, sample, filename):
        newFilename = None
        substr = '.wav'

        if filename.endswith(substr):
            newFilename = filename[:-(len(substr))]
        else:
            newFilename = filename

        if not os.path.exists('SampleLibrary/'):
            os.makedirs('SampleLibrary/')

        fullFileName = 'SampleLibrary/' + newFilename + '.wav'
        write(fullFileName, self.sampleRate, sample)

    def load(self, filename):
        sRate, source = read('SampleLibrary/' + filename)
        return sRate, source

