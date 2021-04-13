from AudioDevice import AudioDevice
from Util import Util
from SampLib import sampLib
from Map import Map
from MIDIdevice import MIDIdevice

def main():
    audio = AudioDevice()
    menu = Util()
    library = sampLib()
    midiDevice = MIDIdevice()
    sample = None

    choice = menu.mainMenu()

    #while user chooses not to exit the program
    while(3 != choice):

        #if user chooses to view sample recording options
        if(1 == choice):
            proceed = False

            while(proceed == False):
                samplingChoice = menu.recSampleMenu()
                if(sample == None and samplingChoice == 2):
                    print("***Error: you must first record a sample in order to play it with a MIDI device***")
                else:
                    proceed = True

            #while user chooses not to exit the sample recording menu
            while(3 != samplingChoice):
                sample = None

                #if user chooses to record a sample
                if(1 == samplingChoice):
                    sample = audio.record()
                    sampleActionChoice = menu.newSampleMenu()

                    #if user chooses to preview the recorded sample
                    while(1 == sampleActionChoice):
                        audio.play(sample)
                        sampleActionChoice = menu.newSampleMenu()

                    #if user chooses to save the sample
                    if(2 == sampleActionChoice):
                        filename = input("Save as: ")
                        audio.save(sample, filename)
                        library.addSample(filename)
                        print("\n***Saved***")

                    #if user chooses to discard the sample
                    elif(3 == sampleActionChoice):
                        sample = None
                        print("\n***Sample discarded***")

                #if user chooses to play the recorded sample with a MIDI device
                elif(2 == samplingChoice):
                    rate, sample = audio.load(filename + '.wav')
                    midiIn, midiOut = midiDevice.midiSetup()
                    print("Press key to map sample to: ")
                    startNote = midiDevice.getStartNote(midiIn, midiOut)
                    print("\n StartNote: MIDI note", startNote)
                    midiMap = Map(startNote, sample, rate)
                    midiDevice.playSound(midiIn, midiOut, midiMap, audio)
                    print("\n***Sample loaded***")

                samplingChoice = menu.recSampleMenu()

        #if user chooses to view Sample Library options
        if(2 == choice):
            libraryChoice = menu.sampleLibMenu()

            #while user chooses not to exit the sample library menu
            while(4 != libraryChoice):

                #if user chooses to display a list of all available samples
                if(1 == libraryChoice):
                    library.dispSamples()

                #if user chooses to select a particular sample from the library
                elif(2 == libraryChoice):
                    sampNum = int(input("Enter sample number: "))
                    filename = library.getFilename(sampNum)
                    print('\n***"' + str(filename) + '" selected***')

                    #once a sample is selected from the library...
                    selectedSampleChoice = menu.selectSampleMenu()

                    #while user chooses not to return to the prior menu
                    while(4 != selectedSampleChoice):

                        #if the user chooses to preview the selected sample
                        if(1 == selectedSampleChoice):
                            rate, sample = audio.load(filename)
                            audio.play(sample)

                        #if the user chooses to load the selected sample to MIDI device
                        elif(2 == selectedSampleChoice):
                            rate, sample = audio.load(filename)
                            midiIn, midiOut = midiDevice.midiSetup()
                            print("Press key to map sample to: ")
                            startNote = midiDevice.getStartNote(midiIn, midiOut)
                            print("\n StartNote: MIDI note", startNote)
                            midiMap = Map(startNote, sample, rate)
                            midiDevice.playSound(midiIn, midiOut, midiMap, audio)

                        #if the user chooses to delete the selected sample
                        elif(3 == selectedSampleChoice):
                            filename = library.delSample(sampNum)
                            print("\n***" + filename + " deleted from library***")
                            sample = None

                        selectedSampleChoice = menu.selectSampleMenu()

                #if user chooses to delete a particular sample
                elif(3 == libraryChoice):
                    sampNum = int(input("\nEnter number of sample to be deleted: "))
                    filename = library.delSample(sampNum)
                    print("\n***" + filename + " deleted from library***")

                libraryChoice = menu.sampleLibMenu()

        choice = menu.mainMenu()

main()