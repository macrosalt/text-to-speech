import requests, base64, voice_actor

def send_request(url, input):
    myobj = voice_actor.myobj
    # use self define voice
    # name, clean_input = func(input)
    # myobj = voice_actor.get_voice_actor(name)
    myobj["input"] = {"text": input}
    x = requests.post(url, json = myobj)
    resp = x.json()
    return base64.b64decode(resp["audioContent"])

