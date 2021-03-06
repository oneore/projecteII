import pyaudio
import numpy as np
import wave
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()

global l

l=[]
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

FRAMES_PERBUFF = 2048 # number of frames per buffer
FORMAT = pyaudio.paInt16 # 16 bit int
CHANNELS = 1 # I guess this is for mono sounds
FRAME_RATE = 44100 # sample rate
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=FRAME_RATE,
                input=True,
                frames_per_buffer=FRAMES_PERBUFF) #buffer
frames = []
RECORD_SECONDS = 4
nchunks = int(RECORD_SECONDS * FRAME_RATE / FRAMES_PERBUFF)
for i in range(0, nchunks):
    try:
        data = stream.read(FRAMES_PERBUFF)
    except IOError as ex:
        if ex[1] != pyaudio.paInputOverflowed:
            raise
        data = '\x00' * FRAMES_PERBUFF
    frames.append(data) # 2 bytes(16 bits) per channel

    swidth = 2
    #l=[]
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
    if thefreq < 80 or thefreq > 2500:
        thefreq = 0
    l.append(thefreq)
    plt.plot(i,thefreq,'ro')
    #print ('La freqüència és de %f Hz.' % (thefreq))
#plt.show()
