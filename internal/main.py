import file, api, voice_actor, pickle, sys
from pydub import AudioSegment
from io import BytesIO

# Need the token. can use the one from demo: https://cloud.google.com/text-to-speech
url = 'https://cxl-services.appspot.com/proxy?url=https://us-central1-texttospeech.googleapis.com/v1beta1/text:synthesize&token=03AKH6MRHpobiSNZBojlGaqKYO7ns8lD6O5ae9iPvlZAS1Zh8cin7IMPEC0R1Mkin2SaGvOd5Dgl8MUvxhqB8BNIrQOuWkJXrAGlyiRYrvWrCs6lJ3-Zc7Is48CgX-SQMcQ-ODa8C2tZrf0wJkr3R0HBBAXbNtB8LBIMGKACKy_YOZc2Ik8CQAFUtcGOs8rPw5i6igE7ShiZf8an4Y-wvl-b-7ShbDV9IwpiomYyuQnD42StyVE4vOAq5xoSt3S3wkc5LN4OI29TE2loA0Xw1kgKduX9tk--BalqQ4YEnXANDHrMpi6aNEp4QfHWtuqSNSJgvGKeNljAlLMtJzNTK7MvlDWNeMd4nvT8GqdYltVL3klBfIQvsdtQE0HhK6RhZeS7tZgVM8fro5Zd9BbNJ3G4Pml244oFeBUxmVnkXTwO1HmZDVInv_eU6ObHI3DwHM1Wk75-Vvj68J6s4Ri5frJE7wdxihJ2n9_3tadG9IF6aHZSkVnhW4kWU0a6NS_SbxQIgJJFcfW8lN4BL9PQBJLddMlIVHxRGC4Q'
file_addr = 'input/input.txt'
story_cache_addr = 'story_cache.pkl'

lines = file.read_non_empty_lines(file_addr)
total_num = len(lines)
print("[log]", "total lines number is ", total_num)

story = AudioSegment.empty()
prev_start = 0
if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    prev_start = int(sys.argv[1])
    print("[log] will start from line", prev_start)
    with open(story_cache_addr, 'rb') as f:
        story = pickle.load(f)

i = 0
one_second_silence = AudioSegment.silent(duration=1000) # between the lines
while i < total_num:
    print("[log] processing line ", i)
    # myobj = voice_actor.myobj
    # use self define voice
    name, input = voice_actor.get_va_name_and_txt(lines[i])
    myobj = voice_actor.get_voice_actor(name)
    myobj["input"] = {"text": input}
    if i < prev_start:
        i = i + 1
        continue

    try:
        line_audio = api.send_request(url, myobj)
    except:
        print("[log] err when sending",myobj)
        with open(story_cache_addr, 'wb') as f:
            pickle.dump(story, f)
            print("[log] successfully cache current story until line:", i)
            quit()
    sound = AudioSegment.from_ogg(BytesIO(line_audio))
    story += sound + one_second_silence 
    i = i + 1

file_handle = story.export("output.mp3",
                           format="mp3",
                           bitrate="192k",
                        #    tags={"album": "", "artist": ""},
                           cover="input/cover.jpg"
                           )

print("[log] job success!")

