# Llegeix Arxiu WAV i troba les freqüències
import pyaudio
import wave
import numpy as np

chunk = 2048
l=[]

wf = wave.open("wav/Camila_Cabello-Havana.wav", 'rb')
wf2 = wave.open("wav/Camila_Cabello-Havana.wav", 'wb')
#wf = wave.open("recorded_audio.wav", 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
# use a Blackman window
window = np.blackman(chunk)
# open stream
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = RATE,
                output = True)

# read some data
data = wf.readframes(chunk)
# play stream and find the frequency of each chunk
while len(data) == chunk*swidth:
    # write data out to the audio stream
    stream.write(data)
    # unpack the data and times by the hamming window
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                         data))*window
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    print('1')
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        print("1")
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        l.append(thefreq)
        print ('La freqüència és de %f Hz.' % (thefreq))
    else:
        thefreq = which*RATE/chunk
        l.append(thefreq)
        print ('La freqüència és de %f Hz.' % (thefreq))
    # read some more data
    data = wf.readframes(chunk)
if data:
    stream.write(data)
stream.close()
p.terminate()

print(l)
