import requests, base64, voice_actor, backoff, time

def send_request(url, input):
    time.sleep(1) # control qps
    try: 
        resp = post_url(url, input)
    except requests.exceptions.RequestException as e:
        print("api error for input:", input, "error:",e)
    return base64.b64decode(resp["audioContent"])

@backoff.on_exception(backoff.constant,
                      requests.exceptions.RequestException,
                      interval=5,
                      max_tries=3)
def post_url(url, myobj):
    resp = requests.post(url, json=myobj)
    resp.raise_for_status()
    return resp.json()

