from os import getenv
from pypresence import Client
from dotenv import load_dotenv
from pynput.keyboard import Listener
import platform
import requests


load_dotenv()

TOKEN_URL = "https://discord.com/api/oauth2/token"
REDIRECT_URI = "http://localhost"

CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")
TOKEN = getenv("TOKEN")

if not CLIENT_ID:
    print("CLIENT_ID must be set")
    exit(1)
if not CLIENT_SECRET or not TOKEN:
    print("Either CLIENT_SECRET or TOKEN must be set")
    exit(1)


def exchange_code(code):
    data = {
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
      'grant_type': 'authorization_code',
      'code': code,
      'redirect_uri': REDIRECT_URI
    }
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(TOKEN_URL, data=data, headers=headers)
    r.raise_for_status()
    return r.json()


def authorize():
    auth = c.authorize(CLIENT_ID, ["rpc","rpc.voice.read","rpc.voice.write"])
    grant_code = auth["data"]["code"]
    res = exchange_code(grant_code)

    print(f"Access token: {res['access_token']}")
    print(f"Refresh token: {res['refresh_token']}")

    return res["access_token"]


def list_sounds():
    sounds = c.get_soundboard_sounds()
    print("Available sounds:")
    for sound in sounds["data"]:
        print(f"  {sound['sound_id']} {sound['emoji_name']} {sound['name']}")


def on_press(key):
    num0 = 82 if platform.system() == "Darwin" else 96
    if hasattr(key, "vk") and num0 < key.vk <= num0 + 6:
        c.play_soundboard_sound(key.vk - num0)


if __name__ == "__main__":
    c = Client(CLIENT_ID)
    c.start()
    c.authenticate(TOKEN if TOKEN else authorize())

    voice_channel = c.get_selected_voice_channel()
    if voice_channel["data"] is not None:
        list_sounds()
        with Listener(on_press=on_press) as listener:
            listener.join()
    else:
        print("You must be in a voice channel")
