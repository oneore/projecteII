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

FRAMES_PERBUFF = 1024 # number of frames per buffer   ORIGINAL: 2048
FORMAT = pyaudio.paInt16 # 16 bit int
CHANNELS = 1 # I guess this is for mono sounds
FRAME_RATE = 48000 # sample rate   ORIGINAL: 44100
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=FRAME_RATE,
                input=True,
                frames_per_buffer=FRAMES_PERBUFF) #buffer
frames = []
RECORD_SECONDS = 20  #canciones duran 35s
nchunks = int(RECORD_SECONDS * FRAME_RATE / FRAMES_PERBUFF)

l = [] #lista con todas las frecuencias escuchadas
for i in range(0, nchunks):
    data = stream.read(FRAMES_PERBUFF, exception_on_overflow = False)
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

lista_canciones = ['Amelie_Le_moulin.txt','chopin_nocturne92.txt','mine.txt','Intouchables.txt','Deja vu, Shakira.txt','Shape of you.txt'] #nuestra lista de canciones
adivinanza = ''

def er(record, cancion):
    if len(record) < len(cancion):
        lon = len(record)
    else:
        lon = len(cancion)

    error = 0
    suma = 0
    for i in range (lon):
        if record[i] != '0':
            error += (abs(float(record[i])-float(cancion[i])))**0.5
            suma += 1
    return error/suma

errorMax = 1000
for c in lista_canciones:
    f2 = open(c,'r')
    cancion = f2.read().split('\n')[:-1]
    record = l
    for i in range (0,14): #21.5 frecuencias por segundo, asi tenemos 2s de margen (3*14) antes de que empieze la cancion
        cancion_recortada = cancion
        for z in range (0,100):    #21.5 frecuencias por segundo, asi tenemos 10s de margen (3*70) despues de que empieze la cancion
            error = er(record,cancion_recortada)
            if errorMax > error:
                errorMax = error
                adivinanza = c[:-4]
            cancion_recortada = cancion_recortada[3:]
        record = record[3:]

print(errorMax)
print(adivinanza)
