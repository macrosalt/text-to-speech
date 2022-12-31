import requests, base64

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

def send_request(url, input):
    myobj["input"] = {"text": input}
    x = requests.post(url, json = myobj)
    resp = x.json()
    return base64.b64decode(resp["audioContent"])

