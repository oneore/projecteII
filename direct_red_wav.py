import pyaudio
import numpy as np
import wave
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()
freqs=np.array([0])
p.get_default_input_device_info()
wf = wave.open("WAV's/Camila_Cabello-Havana.wav", 'rb')
swidth = wf.getsampwidth()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
frames = []
RECORD_SECONDS = 10
nchunks = int(RECORD_SECONDS * 44100 / 2048)
for i in range(0, nchunks):
    chunk = 2048
    data = wf.readframes(chunk)
    window = np.blackman(chunk)
    print(data)
    print(window)
    print(swidth)
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),data))*window
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
    if 100<=thefreq<=5000:
        print ('La freqüència és de %f Hz.' % (thefreq))
        plt.plot(i,thefreq,"ro")
    freqs=np.insert(freqs, -1, thefreq)
    a, b = freqs[-1], freqs[-2]
    freqs[-1], freqs[-2] = b, a
plt.show()
