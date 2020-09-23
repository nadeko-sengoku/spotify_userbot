import requests
import json
from constants import Config

body = {"client_id": Config.CLIENT_ID, "client_secret": Config.CLIENT_SECRET,
        "grant_type": "authorization_code", "redirect_uri": "https://example.com/callback",
        "code": Config.INITIAL_TOKEN}
r = requests.post("https://accounts.spotify.com/api/token", data=body)
save = r.json()
to_create = {'bio': Config.INITIAL_BIO, 'access_token': save['access_token'], 'refresh_token': save['refresh_token'],
             'telegram_spam': False, 'spotify_spam': False}
with open('./database.json', 'w') as outfile:
    json.dump(to_create, outfile, indent=4, sort_keys=True)
