from pydub import AudioSegment


def audio_cutting(time_stamp, cutting_range):
    # Open file
    song = AudioSegment.from_wav('test.wav')

    # Slice audio
    # pydub는 milliseconds 단위를 사용한다

    
    first_10_seconds = song[(time_stamp-cutting_range)*1000 : (time_stamp+cutting_range)*1000]



    # up/down volumn    
    beginning = first_10_seconds + 10

    print("hello")
    # Save the result
    # can give parameters-quality, channel, etc
    beginning.export('result.wav', format='wav', parameters=["-q:a", "10", "-ac", "1"])


# 몇초지점에서 자를건지
time_stamp = 5
cutting_range = 2

audio_cutting(time_stamp,cutting_range)

print("오디오 커팅 종료")
