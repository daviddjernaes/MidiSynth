Group Members: 
David Djernaes   djernaes@pdx.edu
Scott Rubey     scrubey@pdx.edu

Project Name: MIDI Sampling Synth


Project description: 
This program allows the user to record an audio sample, store it in a Sample Library, and play that sample from
a MIDI keyboard/controller.  


How to build and run:  
The program is broken into six files: Main.py, Util.py, AudioDevice.py, MIDIdevice.py, Map.py and SampLib.py.  
Some of these files require the use of the following external Python libraries: sound device, spicy, pyrubberband,
rtmidi, rtmidi.midiutil, pygame, numpy and os.  In order to run the program, one must simply run it in their IDE of 
choice, or type python3 Main.py if running from the command line.

Program flow is as follows:  from the main menu, the user may choose to either record a new sample or explore the
Sample Library.  If the user wishes to record a new sample, they may choose “Start recording” on the following menu.
The sample recorder will count down from 3, then record for exactly 2 seconds.  One may then preview their recorded
sample, save it to the Sample Library, or discard it.  Should the user decide to save the sample, they can then either
play it with a MIDI device through the current menu, or they may choose to edit the sample using their editor of choice
(i.e. Audacity) and access it later via the Sample Library.  

Please note: the user is encourage to load their sample into an audio editor like Audacity to trim any leading/trailing
silence and/or reduce noise.  (This functionality was explored during the development of this program, but remains 
incomplete.)  One must close the program while they are editing their sample, then re-open it once the file has been 
updated; they will find the file in their SampleLibrary folder in the working directory (if a SampleLibrary has not been 
created prior to running the program for the first time, it will be automatically created for them once they save their 
first sample).  Once a file has been edited, it should be exported back to the SampleLibrary folder in the working 
directory as a 32-bit float PCM .wav file.  The user may now access the sample in their Sample Library through the 
course of regular program flow.  

The Sample Library menu, as access via the Main Menu, allows the user to display their sample list, select a sample
from that list by entering its corresponding sample number, or delete a sample, also by entering its corresponding
sample number.  Should the user decide to select a sample, they may then preview that sample, load it to a MIDI
device or delete it via the current menu system.

Loading a sample to a MIDI device is simple.  First, the MIDI device must be connected and powered on.  The user
will be asked if they would like to create a virtual MIDI input port, to which they should answer ’n’.  They will then be
given a list of available MIDI input ports, to which they should answer with the corresponding number.  The same two 
questions will be asked with regard to selecting a MIDI output port; answers should remain the same.  The user will
then be prompted to play the MIDI controller key they would like their sample mapped to.  (For instance, if the sample
consists of a plucked “A” string on a guitar, the user might choose to press an “A” on their MIDI keyboard.)  It will take
several seconds for the sample to be mapped to each key of the MIDI controller; the user will be prompted once their
sample is ready for playback.  Should the user decide to return to the previous menu, they may press Contol-C at any
time.

This concludes standard program flow.


Testing:  unit tests were written on a number of functions; all tests passed as intended.  Due to the tester’s inexperience
with unit testing, this was a positive learning experience, however he remained uncertain of how to apply greater
coverage given the object/return types of certain functions.  This will be an area for exploration moving forward. 
Extensive testing was performed as it relates to standard program flow; the tester spent a great deal of time attempting
to “break” the program.  As a result, errors in program flow (i.e. menu selections) are now handled with appropriate 
messages and prompts, and no fatal errors were found in the program’s present form.  (The sole exception to this might 
occur if the user attempts to access a MIDI device that is not currently connected; attempts were made at rectifying the 
problem, to no avail.)  A PDF reflecting unit test output has been included with our submission.


Results: overall, we are quite satisfied with how far we were able to get on this project with no prior experience in computer
audio.  It seemed a tall order at the beginning of this term to build a working sampler, however we appreciated the
challenge and found a number of useful external libraries that helped tremendously in its development to this point.  Of
course, the resulting program is only a bare-bones approximation of the types of hardware/software we are accustomed
to using, and there are a number of features we would like to improve upon moving forward.  These include (but are not 
limited to) the following.  1) We would like to implement the ability to start and stop sample recording as triggered via a
key-stroke (such as by pressing the space-bar).  This would allow for more flexibility with recording longer or shorter samples.
2) We had explored basic sample editing for the purpose of trimming leading/ending silence and reducing noise in our sample.
It would be nice to create useable samples solely within our sampler’s framework, rather than having to export to an external
editor.  3) Velocity response would be one of the first things we would implement were we to pick this back up in the future.
As it stands, samples can only be triggered via the MIDI device at a constant velocity.  4) It would be nice to implement ADSR
and basic effects, such as reverb and compression.  5) In the Sample Library, our system currently numbers samples on the
fly; i.e. a sample’s number in the library might change as new samples are recorded, and as the program is closed and re-
opened.  It would be nice to set up ‘sound banks’ in which sample numbers/locations are persistent.  On this note, it might
also be of benefit if the user had the capability of setting up file hierarchies for organization of their samples.

We find this to have been a very positive experience with a result that exceeded our expectations, and look forward to
completing further work on this in the future.
