import copy

myobj = {
  "audioConfig": {
    "audioEncoding": "OGG_OPUS",
    "effectsProfileId": [
      "small-bluetooth-speaker-class-device"
    ],
    "pitch": 0,
    "speakingRate": 1
  },
  "input": {
    "text": "hello world"
  },
  "voice": {
    "languageCode": "en-US",
    "name": "en-US-Neural2-C"
  }
}

voice_actor_list = [
    "en-US-Neural2-A",
    "en-US-Neural2-C",
    "en-US-Neural2-D",
    "en-US-Neural2-E",
    "en-US-Neural2-F",
    "en-US-Neural2-G",
    "en-US-Neural2-H",
    "en-US-Neural2-I",
    "en-US-Neural2-J"
]

cur_voice_actor_index = 0
voice_actor_map = {}

def get_voice_actor(name):
    global myobj
    global voice_actor_list
    global cur_voice_actor_index
    global voice_actor_map
    
    res = copy.deepcopy(myobj)
    if name not in voice_actor_map:
        # get in round robin
        voice_actor_map[name] = voice_actor_list[cur_voice_actor_index]
        cur_voice_actor_index = (cur_voice_actor_index + 1) % len(voice_actor_list)
    
    res["voice"]["name"] = voice_actor_map[name]
    return res

def get_va_name_and_txt(input):
    splits = input.split(":", 1)
    if len(splits) == 1:
        return "default", splits[0]
    return splits[0], splits[1]