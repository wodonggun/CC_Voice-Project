import warnings
warnings.filterwarnings('ignore',category=RuntimeWarning) #ffmpeg error control
from pydub import AudioSegment


def audio_cutting(time_stamp, cutting_range):
    # Open file
    song = AudioSegment.from_wav('test.wav')

    # Slice audio
    # pydub는 milliseconds 단위를 사용한다

    #cutting 범위 언더플로우 방지 
    start_time = max(time_stamp-cutting_range,0)
    #cutting 범위 오버플로우 방지
    end_time =   min(time_stamp+cutting_range,len(song) / (1000))


    my_audio = song[(start_time)*1000 : (end_time)*1000]



    # up/down volumn    
    beginning = my_audio + 10

    # Save the result
    # can give parameters-quality, channel, etc
    beginning.export('result.wav', format='wav', parameters=["-q:a", "10", "-ac", "1"])




time_stamp = 5
cutting_range = 2

audio_cutting(time_stamp,cutting_range)

print("오디오 커팅 종료")
