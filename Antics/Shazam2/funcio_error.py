import pyaudio
import numpy as np
import wave
from error import *
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()
freqs=[]
freqs_t=[]
p.get_default_input_device_info()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=2048)
frames = []
RECORD_SECONDS = 10
nchunks = int(RECORD_SECONDS * 44100 / 2048)
for i in range(0, nchunks):
    time=i
    try:
        data = stream.read(2048)
    except IOError as ex: #error que ens dona (Input Overflowed)
        if ex[1] != pyaudio.paInputOverflowed:
            raise
        data = '\x00' * 2048
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
        #plt.plot(i,thefreq,"ro")
        freqs.append(thefreq)
        freqs_t.append([time, thefreq])
#plt.show()

songs = ['new_rules.txt','shape_of_you.txt','idgaf.txt','havana.txt'] #llista de cançons
sum=0
distMax=100000000
for arxiu in songs:
    f = open(arxiu,'r')
    songs = f.read().split('\n')[:-1]
    record = freqs_t
    for num in range(0,len(songs)-len(record)):
        songs_tallat=songs[num:len(record)+num]
        record = freqs_t
        for punt in record:
            if len(songs_tallat)!=0 and len(record)!=0:
                node, dist = closest_node(punt, songs_tallat)
                sum+=dist
                print('PATATAAAAAAAAA')
                songs_tallat.remove(str(node))
                record.remove(punt)
                print(record)
        if distMax>sum:
            distMax=sum
            song=arxiu[:-4]

print(distMax)
print(sum)
