import requests, base64, voice_actor

def send_request(url, input):
    # myobj = voice_actor.myobj
    # use self define voice
    name, input = get_va_name_and_txt(input)
    myobj = voice_actor.get_voice_actor(name)
    myobj["input"] = {"text": input}
    x = requests.post(url, json = myobj)
    resp = x.json()
    return base64.b64decode(resp["audioContent"])

def get_va_name_and_txt(input):
    splits = input.split(":", 1)
    if len(splits) == 1:
        return "default", splits[0]
    return splits[0], splits[1]
