import pyaudio
import numpy as np
import wave
import glob, os
from lcd import *

p = pyaudio.PyAudio()
os.chdir("txt")

clear_screen()

CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
frames = []
l = [] #lista con todas las frecuencias escuchadas

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    swidth = 2
    chunk = CHUNK
    window = np.blackman(chunk)
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                         data))*window
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
    else:
        thefreq = which*RATE/chunk
    l.append(thefreq)

stream.stop_stream()
stream.close()
p.terminate()

guess = ''
guess_song = ''

def er(record, song):
    if len(record) < len(song):
        lon = len(record)
    else:
        lon = len(song)
    error = 0
    sum = 0
    for i in range (lon):
        if record[i] != '0':
            error = (abs(float(record[i])-float(song[i])))**0.5
            if error<3:
                sum += 1
    return sum
sumes=[]
for c in glob.glob("*.txt"):
    f2 = open(c,'r')
    song = f2.read().split('\n')[:-1]
    record = l
    sumMin = 1
    for i in range (0,14): #21.5 frecuencias por segundo, asi tenemos 2s de margen (3*14) antes de que empieze la cancion
        cut_song = song
        for z in range (0,72):    #21.5 frecuencias por segundo, asi tenemos 10s de margen (3*70) despues de que empieze la cancion
            sum = er(record,cut_song)
            if sumMin < sum:
                sumMin = sum
                guess = c[:-4]
            cut_song = cut_song[3:]
        record = record[3:]
    sumes.append([sumMin, guess])
    sumes.sort(reverse = True, key=lambda x: x[0])
guess=sumes[0][1].split('_')
sumMin=sumes[0][0]
print(sumes)
for i in range(len(guess)):
    guess_song+=(str(guess[i]) + ' ')
    if len(guess_song)>15:
        guess_song1=guess_song[0:15]
        guess_song2=guess_song[15:]
        guess_song=guess_song1 + "\n" + guess_song2
if sumes[1][0]/sumes[0][0]<0.8 and sumes[0][0]-sumes[1][0]>5:
    print(sumMin)
    print(guess_song)
    missatge(guess_song)
else:
    print("No s'ha pogut trobar")
    missatge(" No s'ha pogut\n     trobar")
