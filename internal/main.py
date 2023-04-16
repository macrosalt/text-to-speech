import file, api
from pydub import AudioSegment
from io import BytesIO

# Need the token. can use the one from demo: https://cloud.google.com/text-to-speech
url = 'https://cxl-services.appspot.com/proxy?url=https://us-central1-texttospeech.googleapis.com/v1beta1/text:synthesize&token=03AKH6MRHMXmz4UvpZI2SD1ji1uvMKX9hJ4O5E0TUvIBnStJNhdSAMJcLrs8vIbN0NRwxwc_oim4MjF2P6-gCRorkHKlqe40fGYOwyqYw5qwtFq2y0K-achTax2rX45no44jAqpMMraVXG9ek7stQ7XupaGQCJBmZi6VnysBcBuh9CPbT7wNMnxBt8nG0TozHEwrLTpqpwFs4ujLyedBYvYoClb0uO4EIZVNobdQOeNgoYaZzhK0N292jjCtJd8nP78hEai6HKY23j-ZvLs666QArdP4gcOmxjDrvA5Vqny-9_Cb02u0AY7-f48deoP7eWNVCSZD9KMJAe2_2Kbfm1Ir8pLZXbiBp8MHsW-luL4ZXvpVdBOBLpk_6ogkDLH9APm1iiDMFFbzUbzAs6kAk_RAjk04CHg4gBmAystMBlCiruX3rYGtosdL76b7cnJyHKlyL0WBOZuy5iTsqM_rSkmNZBa2kugsA3LLLGSvYpaa_Maa2kqdxloMkTEIZ3Jtb4GpJE3WmRPH5nXpAH8LuE0zkjZTsFlDf9zg'
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
                           cover="input/cover.jpg"
                           )

print("[log] job success!")

