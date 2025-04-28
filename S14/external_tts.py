import requests

def speak_text_external(text):
    api_url = "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "YOUR_ELEVENLABS_API_KEY"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        with open("response.mp3", "wb") as f:
            f.write(response.content)
        print("Playing external TTS audio...")
        os.system("start response.mp3")  # For Windows. Use `afplay` on Mac, `mpg123` on Linux.
    else:
        print("Error:", response.text)
