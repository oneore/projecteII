import pyaudio
import numpy as np
import wave
import glob, os

p = pyaudio.PyAudio()
os.chdir("txt")
p.get_default_input_device_info()

{'defaultHighInputLatency': 0.01292517006802721,
 'defaultHighOutputLatency': 0.1,
 'defaultLowInputLatency': 0.002766439909297052,
 'defaultLowOutputLatency': 0.01,
 'defaultSampleRate': 44100.0,
 'hostApi': '0L',
 'index': '0L',
 'maxInputChannels': '2L',
 'maxOutputChannels': '0L',
 'name': u'Built-in Microph',
 'structVersion': '2L'}

FRAMES_PERBUFF = 2048 # number of frames per buffer   ORIGINAL: 2048
FORMAT = pyaudio.paInt16 # 16 bit int
CHANNELS = 1 # I guess this is for mono sounds
FRAME_RATE = 44100 # sample rate   ORIGINAL: 44100
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=FRAME_RATE,
                input=True,
                frames_per_buffer=FRAMES_PERBUFF) #buffer
frames = []
RECORD_SECONDS = 15  #canciones duran 35s
nchunks = int(RECORD_SECONDS * FRAME_RATE / FRAMES_PERBUFF)

l = [] #lista con todas las frecuencias escuchadas
for i in range(0, nchunks):
    data = stream.read(FRAMES_PERBUFF)
    frames.append(data) # 2 bytes(16 bits) per channel

    swidth = 2
    chunk = FRAMES_PERBUFF
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
        thefreq = (which+x1)*FRAME_RATE/chunk
    else:
        thefreq = which*RATE/chunk
    if thefreq < 10 or thefreq > 3000:
        thefreq = 0
    l.append(thefreq)

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
if sumes[1][0]/sumes[0][0]<0.6:
    print(sumMin)
    print(guess_song)
else:
    print("No s'ha pogut trobar la cançó")
