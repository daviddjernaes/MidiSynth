import os
import numpy as np

class sampLib():
    lib = []
    path = 'SampleLibrary/'

    def __init__(self):
        #build array of samples in the library
        for root, dir, files in os.walk(self.path):
            for f in files:
                self.lib.append(f)

        #convert to a numpy array for easy add/delete
        self.lib = np.asarray(self.lib)

    def dispSamples(self):
        if len(self.lib) == 0:
            print("***Library contains no samples***")
        else:
            print("\n", "\u0332".join("Sample Library"))
            for i in range(len(self.lib)):
                print(i,':', self.lib[i])

    def getFilename(self, i):
        return self.lib[i]

    def addSample(self, file):
        fullFileName = file

        if not file.endswith('.wav'):
            fullFileName = file + '.wav'

        self.lib = np.append(self.lib, fullFileName)

    def delSample(self, i):
        filename = self.lib[i]
        #delete file from disk directory
        if self.lib.size > 0:
            os.remove(self.path + self.lib[i])

            #delete from in-memory sample library
            self.lib = np.delete(self.lib, i)

        else:
            print("\n***Error: Library is empty***")

        return filename
