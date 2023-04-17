# text-to-speech
## Preparation
### Prepare API token
* can use the token generated from demo: https://cloud.google.com/text-to-speech
* OR apply TTS API access in GCP. it provides 1 million characters monthly for free

### Prepare material in `input/`
* `input.txt` text file
* `cover.jpg` optional, used for the cover of generated audio file

### Prepare env
```
sudo pip3 install -r requirements.txt
```

## Run
```
python3 internal/main.py
```
* if failure, can start from the previous line #
```
python3 internal/main.py 100
```