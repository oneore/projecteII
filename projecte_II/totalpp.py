import pyaudio
import numpy as np
import wave

p = pyaudio.PyAudio()

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
RECORD_SECONDS = 2
nchunks = int(RECORD_SECONDS * FRAME_RATE / FRAMES_PERBUFF)
for i in range(0, nchunks):
    data = stream.read(FRAMES_PERBUFF)
    frames.append(data) # 2 bytes(16 bits) per channel
    wf = wave.open('recorded_audio_inst.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    print (p.get_sample_size(FORMAT))
    wf.setframerate(FRAME_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
#print("Enregistrament Completat!")
stream.stop_stream()
stream.close()
p.terminate()

def cepstral(arxiu):
    chunk = 2048
    l=[]
    # open up a wave
    wf = wave.open(arxiu, 'rb')
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
        #stream.write(data)
        # unpack the data and times by the hamming window
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
            l.append(thefreq)
            #print ('La freqüència és de %f Hz.' % (thefreq))
        else:
            thefreq = which*RATE/chunk
            l.append(thefreq)
            #print ('La freqüència és de %f Hz.' % (thefreq))
        # read some more data
        data = wf.readframes(chunk)
    if data:
        stream.write(data)
    stream.close()
    p.terminate()
    
#guardar-ho en arxiu wav

wf = wave.open('recorded_audio.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(FRAME_RATE)
wf.writeframes(b''.join(frames))
wf.close()

# Llegeix Arxiu WAV i troba les freqüències



chunk = 2048
l=[]
# open up a wave
wf = wave.open('recorded_audio.wav', 'rb')
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
    #stream.write(data)
    # unpack the data and times by the hamming window
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
        l.append(thefreq)
        #print ('La freqüència és de %f Hz.' % (thefreq))
    else:
        thefreq = which*RATE/chunk
        l.append(thefreq)
        #print ('La freqüència és de %f Hz.' % (thefreq))
    # read some more data
    data = wf.readframes(chunk)

if data:
    stream.write(data)
stream.close()
p.terminate()



llista = l
freq_tract=[]
nota=[]
cont=0

for i in range(1, len(llista)-1):
    if (-10+llista[i+1]<=llista[i]<=10+llista[i+1]):
        nota.append(llista[i+1])
        cont+=1
    else:
        nota=[]
        cont=0
    if cont>=3:
        sum=0
        cont1=0
        for j in nota:
            sum+=j
            cont1+=1
        mitj=sum/cont1
        freq_tract.append(mitj)
        mitj=0
        cont=0
        nota=[]

#print(llista)
#print(freq_tract)

f=open('notes.txt', 'r')
llista=[]
dicc={}
for linian in f:
    linia=linian.strip().split()
    llista.append(linia)
del[llista[0]]
for i in llista:
    dicc[i[1]]=i[0]

#print(dicc)
#print(list(dicc.keys())[0])

llista_notes=[]
llista_freqs=[]
for f in freq_tract:
    A=np.fromiter(dicc.keys(), dtype=float)
    idx=(np.abs(A-f)).argmin()
    a=format(A[idx], '.2f')
    llista_freqs.append(a)
    llista_notes.append(dicc[a])

print(llista_notes)

llista_def=[]
llista_freqs_def=[]
for i in llista_notes:
    if i not in llista_def:
        llista_def.append(i)
for i in llista_freqs:
    if i not in llista_freqs_def:
        llista_freqs_def.append(i)

#print(llista_def)
print(llista_freqs_def)
