import pyaudio
import numpy as np
import wave

p = pyaudio.PyAudio()
freqs=[]
freqs_t=[]
p.get_default_input_device_info()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=2048)
frames = []
RECORD_SECONDS = 50
nchunks = int(RECORD_SECONDS * 44100 / 2048)
for i in range(0, nchunks):
    time=i
    data = stream.read(2048)
    frames.append(data)
    swidth = 2
    chunk = 2048
    window = np.blackman(chunk)
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                         data))*window
    # S'agafen els valors de la FFT i s'eleven al quadrat
    fftData=abs(np.fft.rfft(indata))**2
    # es troba el màxim
    which = fftData[1:].argmax() + 1
    # s'utilitza la interpolació quadràtica al màxim
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # es troba la freqüència
        thefreq = (which+x1)*44100/chunk
    else:
        thefreq = which*44100/chunk
    if 100<=thefreq<=10000:
        #print ('La freqüència és de %f Hz.' % (thefreq))
        print (thefreq)
        freqs.append(thefreq)
        freqs_t.append([time, thefreq])
