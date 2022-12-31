import file, api
from pydub import AudioSegment
from io import BytesIO

# Need the token. can use the one from demo: https://cloud.google.com/text-to-speech
url = 'https://cxl-services.appspot.com/proxy?url=https://us-central1-texttospeech.googleapis.com/v1beta1/text:synthesize&token=03XXXX'
file_addr = 'input/input.txt'

lines = file.read_non_empty_lines(file_addr)
total_num = len(lines)
print("[log]", "total lines number is ", total_num)
i = 0
story = AudioSegment.empty()
one_second_silence = AudioSegment.silent(duration=1000) # between the lines
while i < total_num:
    print("[log] processing line ", i)
    line_audio = api.send_request(url, lines[i])
    sound = AudioSegment.from_ogg(BytesIO(line_audio))
    story += sound + one_second_silence 
    i = i + 1

file_handle = story.export("output.mp3",
                           format="mp3",
                           bitrate="192k",
                        #    tags={"album": "", "artist": ""},
                        #    cover="input/cover.jpg"
                           )

print("[log] job success!")

