import wave
import warnings
warnings.filterwarnings('ignore',category=RuntimeWarning) #ffmpeg error control
from pydub import AudioSegment
import pyaudio


CHANNELS = 1    # 1:MONO  2: STEREO 
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

RECORD_SECONDS = 10   # sampling time


# recording setting
WAVE_OUTPUT_FILENAME = "test.wav"
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, 
                channels=CHANNELS, 
                rate=RATE, 
                input=True, 
                frames_per_buffer=CHUNK)


# recording start
try:
    print("* recording........") 
    frames = []
    for i in range(0, int(RATE/CHUNK     * RECORD_SECONDS)): 
        data = stream.read(CHUNK) 
        frames.append(data)

finally:                
    print("* done recording")
    stream.stop_stream() 
    stream.close() 
    p.terminate() 


# wav_file write
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb') 
wf.setnchannels(CHANNELS) 
wf.setsampwidth(p.get_sample_size(FORMAT)) 
wf.setframerate(RATE) 
wf.writeframes(b''.join(frames)) 
wf.close()


# volume up (Pyaudio can't support Volume)
song = AudioSegment.from_wav('test.wav')
beginning = song+25              # Volue up(25dB)
beginning.export('test.wav', format='wav', parameters=["-q:a", "10", "-ac", "1"])
print("audio volume up.... complete")


